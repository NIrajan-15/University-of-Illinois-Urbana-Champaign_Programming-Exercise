# Training Manager

This Python program manages and analyzes training completion data. It provides functionality to count completed trainings, list people who completed specified trainings in a given fiscal year, and identify expiring or expired trainings.

## Features

- Count the number of people who completed each training.
- List people who completed specified trainings in a specified fiscal year.
- Identify people with expiring or expired trainings of specified year.

## Getting Started

### Prerequisites

- Python 3.x

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/training-manager.git

### Navigate to the Project Directory

### Run the Program
 - python main.py

# Reports

Reports generated by the program can be found in the `reports` directory.

## Training Count Report
- **File**: Training Completion Count.json
- **Description**: Lists each completed training along with a count of how many people have completed that training.

## Fiscal Year Trainings Report
- **File**: Completed Training by Fiscal Year 2024.json
- **Description**: Lists all people who completed each specified training in the specified fiscal year.
  ### parameters
  - **Trainings**:
    - "Electrical Safety for Labs"
    - "X-Ray Safety"
    - "Laboratory Safety Training"
  - **Fiscal Year**: 2024

## Expired Trainings Report
- **File**: Expired or Expiring trainings.json
- **Description**: Finds people with expired or expiring soon trainings based on a specified date.
  - **Date**: Oct 1st, 2023

