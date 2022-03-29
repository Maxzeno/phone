from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import FileField
from flask_uploads import configure_uploads, IMAGES, UploadSet

app = Flask(__name__)

app.config['SECRET_KEY'] = 'thisisasecret'
app.config['UPLOADED_IMAGES_DEST'] = 'uploads/images'

images = UploadSet('images', IMAGES)
configure_uploads(app, images)


class MyForm(FlaskForm):
    image = FileField('image')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = MyForm()
    if form.validate_on_submit():
        filename = images.save(form.image.data)
        return f'Filename: {filename}'
    return render_template('index.html', form = form)

if __name__==('__main__'):
    app.run(debug=True)




    

# from flask import Flask
# from werkzeug.utils import secure_filename
# from flask_uploads import UploadSet, configure_uploads, IMAGES
# import flask_fileupload
# # import flask_ext ## for subdomain
# # import flask_fileupload
# import werkzeug.utils
# import werkzeug

# app = Flask(__name__)




# # print(dir(werkzeug.utils))

# print(dir(werkzeug))



# if __name__ == '__main__':
#     app.run(debug=True)


"""
    brand
    year
    availability
    price
    network_2g
    network_3g
    network_4g
    network_5g
    sim_size
    sim_multiple
    body_form_factor
    body_keyboard
    body_height
    body_width
    body_weight
    body_thickness
    body_ip_certificate
    body_color
    body_back_material
    body_frame_material
    os
    os_version
    cpu_freq
    cpu_cores
    chipset
    ram
    storage
    card_slot
    display_resolution
    display_size
    display_density
    display_technology
    display_notch
    display_high_refresh_rate
    display_hdr
    main_camera_resolution
    main_camera_f_number
    main_camera_cameras
    main_camera_ois
    main_camera_telephoto
    main_camera_ultrawide
    main_camera_flash
    main_camera_video
    selfie_camera_resolution
    selfie_camera_dual_camera
    selfie_camera_ois
    selfie_camera_front_flask
    selfie_camera_pop_up_camera
    selfie_camera_under_display
    sensor_accelerometer
    sensor_compass
    sensor_gyro
    sensor_compass
    sensor_proximity
    sensor_heart_rate
    sensor_fingerprint
    wlan
    bluetooth
    gps
    nfc
    infrared
    fm_radio
    usb_type_c
    battery_capacity
    battery_removable
    charging_wired
    charging_wireless
    misc_free_text
    misc_order
    misc_reviewed_only
    new
"""