from google import genai
from config import API_KEY
from prompts import SYSTEM_PROMPT
import logging

# Logging
logging.basicConfig(
    filename="chatbot.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Gemini Client
client = genai.Client(api_key=API_KEY)

# Conversation Memory
chat_history = []

# Mock Order Database
orders = {
    "12345": "Shipped",
    "67890": "Delivered",
    "11111": "Out for Delivery",
    "22222": "Processing"
}


def track_order(order_id):
    return orders.get(order_id, "Order not found")


def chat(user_input):

    chat_history.append({
        "role": "user",
        "content": user_input
    })

    conversation = SYSTEM_PROMPT + "\n\n"

    for msg in chat_history:
        conversation += (
            f"{msg['role']}: "
            f"{msg['content']}\n"
        )

    try:

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=conversation
        )

        bot_reply = response.text

        chat_history.append({
            "role": "assistant",
            "content": bot_reply
        })

        return bot_reply

    except Exception as e:
        logging.error(str(e))
        
        return f"ERROR: {str(e)}"


def process_query(user_input):

    logging.info(user_input)

    if "track order" in user_input.lower():

        order_id = user_input.split()[-1]

        return track_order(order_id)

    return chat(user_input)