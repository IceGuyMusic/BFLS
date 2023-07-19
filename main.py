import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def find_skiprows(file_name):
    with open(file_name, 'r', encoding='ISO-8859-1') as f:
        for i, line in enumerate(f):
            if 'R.Time (min)\tIntensity' in line:
                return i
    return None

def analyze_hplc_data(file_name, retention_times):
    # Find the number of rows to skip
    skiprows = find_skiprows(file_name)
    if skiprows is None:
        print(f'Could not find data start in {file_name}')
        return None

    print(f'Loading data from {file_name} skipping {skiprows} lines')

    # Load the HPLC data with 'ISO-8859-1' encoding and skipping the appropriate number of lines
    hplc_data = pd.read_csv(file_name, sep='\t', encoding='ISO-8859-1', skiprows=skiprows)

    print(f'Loaded data with columns: {hplc_data.columns}')

    # Convert columns to appropriate data types
    hplc_data['R.Time (min)'] = pd.to_numeric(hplc_data['R.Time (min)'], errors='coerce')
    hplc_data['Intensity'] = pd.to_numeric(hplc_data['Intensity'], errors='coerce')

    # Remove baseline noise
    hplc_data['Intensity'] = hplc_data['Intensity'].apply(lambda x: x if x > 4 else 0)

    # Select the peak between the specified retention times
    peak_data = hplc_data[(hplc_data['R.Time (min)'] >= retention_times[0]) & (hplc_data['R.Time (min)'] <= retention_times[1])]

    # Calculate the area under the peak
    peak_area = np.trapz(peak_data['Intensity'], peak_data['R.Time (min)'])

    # Plot the peak
    plt.figure(figsize=(10, 6))
    plt.plot(peak_data['R.Time (min)'], peak_data['Intensity'])
    plt.fill_between(peak_data['R.Time (min)'], peak_data['Intensity'], color='skyblue', alpha=0.4)
    plt.xlabel('Retention Time (min)')
    plt.ylabel('Intensity')
    plt.title('HPLC Peak')
    plt.grid(True)
    plt.savefig(file_name.replace('.txt', '_peak_plot.png'))

    return peak_area

# Load the analysis parameters from the JSON file
with open('config/config.json', 'r') as f:
    analysis_parameters = json.load(f)

# Create a DataFrame to hold the results
results = pd.DataFrame(columns=['Sample Name', 'Peak Area'])
# Analyze each file
for file_name in analysis_parameters['files']:
    file_name = "RAW_DATA/" + file_name 
    peak_area = analyze_hplc_data(file_name, analysis_parameters['retention_times'])
    if peak_area is not None:
        new_row = pd.DataFrame({'Sample Name': [file_name], 'Peak Area': [peak_area]})
        results = pd.concat([results, new_row], ignore_index=True)

# Save the results to a CSV file
results.to_csv('Output/db/results.csv')
