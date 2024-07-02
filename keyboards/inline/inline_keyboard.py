from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

like = InlineKeyboardButton(
    text='+',
    callback_data='like'
)

dislike = InlineKeyboardButton(
    text='-',
    callback_data='dislike'
)

inline_keyboard_agree = InlineKeyboardMarkup(
    inline_keyboard=[[like],
                     [dislike]]
)

jokes = InlineKeyboardButton(
    text='😉ЖЕНСКОЕ🤫',
    callback_data='-1002072920591'
)

recepies = InlineKeyboardButton(
    text='Только для девочек🤫',
    callback_data='-1002232311428'
)

inline_keyboard_choose_category = InlineKeyboardMarkup(
    inline_keyboard=[[jokes],
                     [recepies]]
)