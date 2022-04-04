from flask import Flask, render_template, redirect, request
from flask_wtf import FlaskForm
from wtforms import FileField
from flask_uploads import configure_uploads, IMAGES, UploadSet
from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage
import os
app = Flask(__name__)

app.config['SECRET_KEY'] = 'thisisasecret'
app.config['UPLOADED_IMAGES_DEST'] = '.\\inspiration'



images = UploadSet('images', IMAGES)
configure_uploads(app, images)


class MyForm(FlaskForm):
    image = FileField('image')

@app.route('/test', methods=['GET', 'POST'])
def test():
    form = MyForm()
    if form.validate_on_submit():
        img = form.image.data
        filename = secure_filename(img.filename)
        print(img.filename, filename)
        print(dir(FileStorage))
        print(help(FileStorage))

        thefile = os.path.join(app.config['UPLOADED_IMAGES_DEST'], filename)
        print(thefile)
        FileStorage.save(thefile)
        # filename = images.save(img)
        return f'Filename: {filename}'
        # return redirect('/')
    return render_template('test.html', form=form)



@app.route('/', methods=['GET', 'POST'])
def index():
    form = MyForm()
    if form.validate_on_submit():
        img = form.image.data
        print(img, type(img))
        filename = images.save(img)
        return f'Filename: {filename}'
        # return redirect('/')
    return render_template('test.html', form=form)


if __name__==('__main__'):
    app.run(debug=True)

