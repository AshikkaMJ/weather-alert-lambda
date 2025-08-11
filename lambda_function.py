import json
import urllib.request
import boto3
import os

sns_topic_arn = os.environ['SNS_TOPIC_ARN']
api_key = os.environ['WEATHER_API_KEY']
city = os.environ['CITY_NAME']

def lambda_handler(event, context):
    sns = boto3.client('sns')
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    with urllib.request.urlopen(url) as response:
        data = json.loads(response.read())
    
    weather_desc = data['weather'][0]['description']
    temp = data['main']['temp']
    
    # Debug logs
    print(f"Weather Description: {weather_desc}")
    print(f"Temperature: {temp}")
    
    alert_conditions = ['storm', 'rain', 'thunderstorm', 'drizzle', 'snow', 'clouds']
    alert_triggered = any(cond in weather_desc.lower() for cond in alert_conditions)
    
    if alert_triggered:
        message = f"Weather Alert for {city}!\nCondition: {weather_desc}\nTemperature: {temp}°C"
        sns.publish(TopicArn=sns_topic_arn, Message=message, Subject="Weather Alert!")
        return {
            'statusCode': 200,
            'body': json.dumps('Alert sent.')
        }
    else:
        return {
            'statusCode': 200,
            'body': json.dumps('No alert needed.')
        }