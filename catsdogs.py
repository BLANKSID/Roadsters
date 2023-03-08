import flask
from flask import Flask, render_template, request, jsonify
from keras.preprocessing import image
from werkzeug.utils import secure_filename
import os

app=Flask(__name__,template_folder='templates')
app.config["DEBUG"] = True




@app.route('/', methods=['GET'])
def home():
  return render_template('index.html')

@app.route('/about')
def about():
    return render_template('aboutus.html')

@app.route('/predict', methods=['POST'])
def upload():
    
    # Get the image from the POST request
    file = request.files['image']  # retrieve the image file from the form
    if file:
        filename = 'input.jpg'
        file.save(filename)  # save the file to disk
    # Preprocess the image as needed
    

    test_image = image.load_img('input.jpg', target_size = (256, 256)) 
    test_image = image.img_to_array(test_image)
    test_image = np.expand_dims(test_image, axis = 0)

    #predict the result
    result = model.predict(test_image)

    predicted_img=np.argmax(result, axis=3)[0,:,:]
    plt.title('Prediction on test image')
    plt.imshow(predicted_img)
    plt.savefig('./static/books', dpi=200)
    for filename in os.listdir('.static/'):
          # not to remove other images
            os.remove('./static/books')

    plt.savefig('./static/books', dpi=200)
    numb = 1
    response = {
        
        'value':numb
    }
    return jsonify(response) 
    
    
if __name__ == '__main__':
    app.run(debug = False)