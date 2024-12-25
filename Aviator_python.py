import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Set up logging to keep track of errors
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# Function to handle the /start command
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Welcome to the Aviator prediction bot! Type /predict to get a prediction.')

# Function to handle the /predict command
def predict(update: Update, context: CallbackContext) -> None:
    prediction = make_prediction()  # Call your prediction function here
    update.message.reply_text(f'Your Aviator prediction is: {prediction}')

# Example prediction logic (replace this with your own logic)
def make_prediction() -> str:
    # Dummy logic: For example, randomly predict a multiplier between 1x and 10x
    import random
    return f'{random.randint(1, 10)}x'

# Main function to handle the bot and commands
def main() -> None:
    # Create an updater using your bot token
    updater = Updater("7571631597:AAGN_ZokomBQVYEgWpnFKxDJG0XzFutaeHk")

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Register command handlers
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("predict", predict))

    # Start the bot
    updater.start_polling()

    # Run the bot until you send a stop command
    updater.idle()

if __name__ == '__main__': 
    main()