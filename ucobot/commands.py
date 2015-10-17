from ucobot import bot
from ucobot.model import user
import random
#Para la realización del teclado
from telebot import types

user_dict = {}

# Handle '/start' and '/help'
@bot.message_handler(commands=['hola', 'start'])
def send_welcome(message):
    user.search_user(message.from_user)
    bot.reply_to(message, """\
Hola, bienvenido al bot del fucking master Juanra!\
""")

@bot.message_handler(commands=['help'])
def send_help(message):
    user.search_user(message.from_user)
    bot.reply_to(message, """\
/hola El bot saluda
/juanra El bot muestra a juanra
/instachica El bot muestra una chica aleatoria
/piropo El bot muestra un piropo\
""")

@bot.message_handler(commands=['juanra'])
def send_juanra(message):
	chat_id = message.chat.id
	photo = open('/Users/Juanra/Desktop/Juanra/juanra.jpg', 'rb')  
	bot.send_photo(chat_id, photo)

@bot.message_handler(commands=['instachica'])
def send_instachica(message):
	chat_id = message.chat.id
	aleatorio=str(random.randint(1, 18))
	user_dict[chat_id] = aleatorio
	photo = open('/Users/Juanra/Desktop/chicas/'+aleatorio+'.jpeg', 'rb')  
	markup=types.ReplyKeyboardMarkup()
	markup.add('1','2', '3', '4', '5')
	msg=bot.send_photo(chat_id, photo, reply_markup=markup)
	#registra el numero ultimo es como un scanf
	bot.register_next_step_handler(msg, process_name_step)
	#markup=types.ReplyKeyboardHide(selective=False)
	#bot.send_photo(chat_id, photo, reply_markup=markup)
	#bot.send_message(chat_id, message, None, None, markup)


def process_name_step(message):
    chat_id = message.chat.id
    nota = int(message.text)

    usuario = message.from_user
    chica = user_dict[chat_id]
    user.guardar_voto(usuario, chica, nota)
    msg = bot.reply_to(message, 'Voto guardado')

@bot.message_handler(commands=['piropo']) 
def command_miramacho(message): 
    cid = message.chat.id # Guardamos el ID de la conversación para poder responder.
    numero = random.randrange(10) 
    frases ={1:"Vas to burlao",
    2:" Tú si que tienes un buen polvo y no lo que tiene el bote de colacao!",
    3:"De ese bacalao se aprovechan hasta las espinas",
    4:"De que horno ha salido semejante bollo!",
    5:"Bonita, te llaman la gripe, has pasado por todos",
    6:"Perfecta parrilla para asar mi morcilla!",
    7:"Mi novia no es puta me lo ha dicho ella",
    8:"Bonita, te llaman la gripe, has pasado por todos",
    9:"Bonita, te llaman la gripe, has pasado por todos"
    }
    mensaje = frases[numero]
    bot.send_message( cid, mensaje)


