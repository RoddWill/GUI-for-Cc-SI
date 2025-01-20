# Cc and SI Prediction Application

![Presentation2](https://github.com/user-attachments/assets/de99065e-d28f-428a-8d54-672c78ad01cd)


This application predicts the **Compression Index (Cc)** and **Swelling Index (SI)** based on the input soil parameters. The application calculates the **Plasticity Index (PI)** automatically using the **Liquid Limit (LL)** and **Plastic Limit (PL)**, which are required for the prediction models. These values, along with the **Initial Void Ratio (eo)** and **Natural Water Content (wn)**, are used to generate accurate predictions for the soil behavior.

## Features

- **Automatic PI Calculation**: 
  The application automatically calculates the **Plasticity Index (PI)** as the difference between the **Liquid Limit (LL)** and **Plastic Limit (PL)**.
  
- **Real-Time Predictions**: 
  Based on the input parameters, the application predicts the **Compression Index (Cc)** and **Swelling Index (SI)** values using pre-trained models.

- **Copy All Data**: 
  The application allows users to copy all input data and prediction results to the clipboard for easy sharing.

## How to Use

1. **Input Parameters**:
   - Enter the following soil parameters:
     - **Initial Void Ratio (eo)**: The initial void ratio of the soil.
     - **Natural Water Content (wn)**: The natural water content of the soil (in %).
     - **Liquid Limit (LL)**: The liquid limit of the soil (in %).
     - **Plastic Limit (PL)**: The plastic limit of the soil (in %).
   
2. **Automatic PI Calculation**:
   - As you enter the **Liquid Limit (LL)** and **Plastic Limit (PL)**, the **Plasticity Index (PI)** will be calculated automatically and displayed in the interface.

3. **Predict Cc and SI**:
   - Click the **Predict Cc & SI** button to calculate the **Compression Index (Cc)** and **Swelling Index (SI)** based on the provided parameters.

4. **View Results**:
   - The predicted values for **Cc** and **SI** will be displayed in the **Results** section.

5. **Copy All Data**:
   - Click the **Copy All** button to copy all input values and prediction results to the clipboard. This can be shared or saved for later use.

## Installation

1. **Clone the repository**:
   ```
   git clone https://github.com/your-username/soil-prediction-app.git
   ```

2. **Install required dependencies**:
   Ensure you have **Python 3.x** and **pip** installed. Then, install the dependencies:
   ```
   pip install -r requirements.txt
   ```

3. **Place the required files**:
   - Ensure the following files are in the correct directory:
     - **logo.png**: Application logo for the window icon.
     - **Presentation2.png**: Application logo for the top banner.
     - **Cc_Random Forest_best.pkl**: Pre-trained model for predicting **Cc**.
     - **SI_Random Forest_best.pkl**: Pre-trained model for predicting **SI**.

4. **Run the Application**:
   Run the Python script:
   ```
   python app.py
   ```

## Example Input

| Parameter              | Value   |
|------------------------|---------|
| Initial Void Ratio (eo) | 35    |
| Natural Water Content (wn) | 15.0   |
| Liquid Limit (LL)       | 30.0    |
| Plastic Limit (PL)      | 21.0    |

### Example Output:

```
Predicted Compression Index (Cc): 0.2345
Predicted Swelling Index (SI): 0.5678
```

## Troubleshooting

- **Model Loading Error**:
  If there is an issue loading the models, ensure that the paths to the models (`Cc_Random Forest_best.pkl` and `SI_Random Forest_best.pkl`) are correct, and the files are not corrupted.

- **Negative PI Error**:
  If the calculated **Plasticity Index (PI)** is negative, it will display an error message, as the **Liquid Limit (LL)** must always be greater than or equal to the **Plastic Limit (PL)**.

- **Missing Input Data**:
  If any input field is left empty, the application will prompt you to fill it in before proceeding.

## License

This project is licensed under the **Creative Commons Zero v1.0 License**.

## Acknowledgements

- The pre-trained **Gradient Boosting models** were developed and trained for soil compaction prediction.
- Thanks to **scikit-learn** and **Tkinter** for providing the necessary tools and libraries for this project.

## Contact

For questions or suggestions, please contact:

- **Developed and Designed by**: Rod Will
- **Email**: [rhudwill@gmail.com]

## References

- **Soil Mechanics and Foundations** (for understanding the theoretical background of soil compaction).
- **Random Forest Model for Predictive Analytics** (for insights into using Gradient Boosting for prediction).

## How to Contribute

Contributions to improve this application are welcome! Feel free to fork this repository, create a branch, and submit a pull request with your suggestions or improvements.

## Screenshots
![Cc_SI_GUI](https://github.com/user-attachments/assets/be1afbbf-cc51-4e26-b0cd-8405ea87197d)

---
### License

This project is licensed under the **Creative Commons Zero v1.0 License**.

--- 
