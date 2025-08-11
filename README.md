# Weather Alert Lambda

This project contains an AWS Lambda function that checks the current weather for multiple cities using the OpenWeatherMap API and sends alerts via Amazon SNS if certain conditions are met.

## Features
- Checks weather for **Ooty** and **Theni**
- Alerts for weather conditions like: storm, rain, thunderstorm, drizzle, snow, clouds
- Sends notifications via SNS to subscribed email addresses
- Can run automatically every hour using **Amazon EventBridge**

---

## Environment Variables
Before deploying the Lambda function, set these environment variables:

| Variable               | Description |
|------------------------|-------------|
| `SNS_TOPIC_ARN`        | ARN of the SNS topic for Ooty alerts — `arn:aws:sns:us-east-1:975050082269:WeatherAlerts` |
| `SNS_TOPIC_ARN_THENI`  | ARN of the SNS topic for Theni alerts — `arn:aws:sns:us-east-1:975050082269:WeatherAlerts_Theni` |
| `WEATHER_API_KEY`      | Your OpenWeatherMap API key — `90b3ee52cd20e1165d5e4e4d23e9e2df` |

---

## How It Works
1. Lambda runs on a schedule (EventBridge rule — hourly)
2. For each city in the configuration:
   - Calls the OpenWeatherMap API
   - Checks if the weather matches alert conditions
   - Publishes a message to the respective SNS topic
3. SNS sends email alerts to subscribed users

---

## Deployment Steps
1. **Create SNS Topics**
   - `WeatherAlerts` (for Ooty)
   - `WeatherAlerts_Theni` (for Theni)
2. **Subscribe Emails**
   - Add each recipient to the correct SNS topic.
3. **Deploy Lambda Function**
   - Upload `lambda_function.py` to AWS Lambda.
   - Set the environment variables listed above.
4. **Create EventBridge Rule**
   - Schedule to run every hour.
   - Set Lambda function as the target.

---
## Example Output (CloudWatch Logs)
City: Ooty, Weather: overcast clouds, Temp: 15.86
Alert sent for Ooty
City: Theni, Weather: overcast clouds, Temp: 28.58
Alert sent for Theni


## License
This project is licensed under the MIT License.
