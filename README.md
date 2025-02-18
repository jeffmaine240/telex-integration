# Daily Motivation Bot for Telex  
**Type:** Interval Integration  

## Description  
The **Daily Motivation Bot** sends motivational quotes daily to inspire and uplift team members, helping to maintain a positive and productive work environment. The bot automatically fetches and delivers a new motivational quote each day, encouraging teamwork and boosting morale.  

## Key Features  
- **Daily Motivational Quotes:** Automatically sends a new motivational quote every day.  
- **Inspiration Boost:** Helps to uplift and inspire team members to stay positive and productive.  
- **Automated Scheduling:** Quotes are delivered at a set interval, ensuring consistent motivation.  
- **Easy Integration:** Seamlessly integrates with Telex channels for hassle-free deployment.  
- **Customizable Settings:** Allows customization of delivery time intervals to fit team schedules.  

## Integration JSON  
```json
{
  "data": {
    "date": {
      "created_at": "2025-02-17",
      "updated_at": "2025-02-17"
    },
    "descriptions": {
      "app_name": "Daily Motivation Bot",
      "app_description": "Sends motivational quotes daily to inspire and uplift team members.",
      "app_logo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSowU4UV3Sncxajn1Smd8UMnTaN9Mm6mtk5NA&usqp=CAU",
      "app_url": "http://web-production-a9a1.up.railway.app",
      "background_color": "#fff"
    },
    "is_active": true,
    "integration_type": "interval",
    "key_features": [
      "Daily Motivational Quotes",
      "Automated Scheduling",
      "Customizable Settings"
    ],
    "category": "communication",
    "author": "jeffmaine",
    "settings": [
      {
        "label": "time interval",
        "type": "text",
        "required": true,
        "default": "* * * * *"
      }
    ],
    "tick_url": "http://web-production-a9a1.up.railway.app/tick"
  }
}
```
## Prerequisites  
- **Python 3.9+**  
- **FastAPI**  
- **HTTPX**  
- **Telex account and channel**  

## Installation  
### 1. Clone the Repository  
```sh
git clone git@github.com:jeffmaine240/telex-integration.git
cd telex-integration
```

### 2. Create a Virtual Environment 
```sh
python3 -m venv venv
source venv/bin/activate  
```

### 3. Install Dependencies
```sh
pip install -r requirements.txt
```

## Usage  
### 1. Run the Application Locally  
```sh
uvicorn main:app --reload
```

### 2. Access the Integration JSON
Open your browser and navigate to: 
```sh
http://127.0.0.1:8000/integration.json
```

check for the json details

## Deployment

The integration is deployed on fly.io and can be accessed here:  
[Live Deployment](https://example-task.fly.dev/)

### 3. Telex Integration
- Add the integration JSON URL in your Telex organization.
- Configure the time interval in the settings (e.g., `* * * * *` for every day).

## Screenshots
![alt text](<Screenshot 2025-02-17 at 20.11.27.png>)