import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences


def predict_feedback(message):
	tokenizer = Tokenizer(num_words=150, oov_token="<OOV>")
	tokenizer.fit_on_texts(message)
	word_index = tokenizer.word_index
	testing_sequences = tokenizer.texts_to_sequences(message)
	testing_padded = pad_sequences(testing_sequences, maxlen=max_length, padding="post", truncating="post")

	testing_padded = np.array(testing_padded)

	model = load_model("Inframind_model.h5")
	return model.predict(testing_padded)

print("Don't Take the Chance - Get the SE Branded Cable: If you purchase this data cable, you need to know that you will receive no real directions or information regarding what to check if nothing works. As directed, I downloaded all of the files from the SE site (70MB on dial up!), and then downloaded all of the user guides. Everything seemed to install ok, but nothing would make my phone be recognized. After that I scoured the SE site for troubleshooting info on their branded cable-in the hope that something would help me figure out the problem. After 2 full days of beating my head against the wall, I finally threw the cable and the useless CD that came with it in the trash.If I had used my brain I would have paid the extra $$ for a SE branded cable and software (and the support that comes along with that). I now have the real deal (SE data cable and software), and guess what? Yep, installation was a breeze and it works beautifully. You really do get what you pay for.")