import axios from 'axios';

const API_URL = 'http://localhost:5000/api';  // Flask Backend URL

// Send query to the backend
export const sendQuery = async (query) => {
  try {
    const response = await axios.post(`${API_URL}/query`, { query });
    return response.data;
  } catch (error) {
    console.error('Error sending query:', error);
    throw error;
  }
};

// Download PDF report
export const downloadPdf = async (response) => {
  try {
    const res = await axios.post(`${API_URL}/download/pdf`, { response }, {
      responseType: 'blob',   // Handle binary file response
    });

    // Create a URL for the blob and trigger download
    const url = window.URL.createObjectURL(new Blob([res.data]));
    const link = document.createElement('a');
    link.href = url;
    link.setAttribute('download', 'report.pdf');
    document.body.appendChild(link);
    link.click();
    link.remove();
    window.URL.revokeObjectURL(url);

  } catch (error) {
    console.error('Error downloading PDF:', error);
    throw error;
  }
};

// Download CSV report
export const downloadCsv = async (response) => {
  try {
    const res = await axios.post(`${API_URL}/download/csv`, { response }, {
      responseType: 'blob',   // Handle binary file response
    });

    // Create a URL for the blob and trigger download
    const url = window.URL.createObjectURL(new Blob([res.data]));
    const link = document.createElement('a');
    link.href = url;
    link.setAttribute('download', 'report.csv');
    document.body.appendChild(link);
    link.click();
    link.remove();
    window.URL.revokeObjectURL(url);

  } catch (error) {
    console.error('Error downloading CSV:', error);
    throw error;
  }
};
