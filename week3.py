import requests
import json
import os

def fetch_user_data():
    url = "https://randomuser.me/api/"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to fetch data")
        return None

def save_data_to_file(data, filename="user_data.json"):
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)
    print("User data saved successfully.")

def load_data_from_file(filename="user_data.json"):
    if os.path.exists(filename):
        with open(filename, "r") as file:
            return json.load(file)
    else:
        return None

def display_user_data(data):
    user = data["results"][0]
    name = f"{user['name']['title']} {user['name']['first']} {user['name']['last']}"
    gender = user["gender"]
    email = user["email"]
    print(f"Name: {name}\nGender: {gender}\nEmail: {email}")

if __name__ == "__main__":
    print("Fetching new user data...")
    user_data = fetch_user_data()
    
    if user_data:
        display_user_data(user_data)
        save_data_to_file(user_data)
    
    print("\nLoading previously saved data...")
    saved_data = load_data_from_file()
    
    if saved_data:
        display_user_data(saved_data)
    else:
        print("No saved data found.")
