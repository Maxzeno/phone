from flask_login import UserMixin, current_user
from datetime import datetime 
from application import db, login_manager#, admin, ModelView


# admin.add_view(ModelView(User, db.session))
        

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


class User(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True) 
    email = db.Column(db.String(80), unique=True, nullable=False) 
    password = db.Column(db.String(255), nullable=False)
    balance = db.Column(db.Float, default=0)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    phone_number = db.Column(db.String(50))
    confirmed_email = db.Column(db.Boolean, default=False)
    suspended = db.Column(db.Boolean, default=False)
    num_of_times_suspended = db.Column(db.Integer, default=0)
    reg_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    country = db.Column(db.String(40))
    ip = db.Column(db.String(20))


class Orders(db.Model):       
    id = db.Column(db.Integer, primary_key=True) 
    user_id = db.Column(db.String(60), db.ForeignKey('user.id'))
    product = db.Column(db.String(60), db.ForeignKey('phones.id'))
    delivered = db.Column(db.Boolean, default=False)
    date_delivered = db.Column(db.DateTime)
    date_ordered = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)


class Address(db.Model):       
    id = db.Column(db.Integer, primary_key=True) 
    user_id = db.Column(db.String(60), db.ForeignKey('user.id'))
    continent = db.Column(db.String(50))
    country = db.Column(db.String(100))
    state = db.Column(db.String(100))
    address = db.Column(db.Text(1024))
    date_added = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)


class Phones(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_added = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    brand = db.Column(db.String(40))
    year = db.Column(db.String(10))
    description = db.Column(db.Text(1000)) 
    phone_image_front = db.Column(db.Text(1024))
    phone_image_back = db.Column(db.Text(1024))
    phone_image_side = db.Column(db.Text(1024))
    name = db.Column(db.String(300))
    price = db.Column(db.Float)
    rating = db.Column(db.Integer)
    features = db.Column(db.PickleType, default={})

    new = db.Column(db.Boolean)
    network = db.Column(db.String(40))
    sim_card_slot_size = db.Column(db.String(40))
    sim_slot_count = db.Column(db.Integer)
    body_form_factor = db.Column(db.String(40)) #bar flip slider
    body_color = db.Column(db.String(40))
    os = db.Column(db.String(40))
    ram = db.Column(db.Integer)
    storage = db.Column(db.Integer)
    display_type = db.Column(db.String(40))
    display_resolution = db.Column(db.String(40))
    camera_resolution = db.Column(db.String(40))
    wlan = db.Column(db.Boolean)
    bluetooth = db.Column(db.Boolean)
    gps = db.Column(db.Boolean)
    fm_radio = db.Column(db.Boolean)
    connector_type = db.Column(db.Boolean) #eg. usb_type_c
    battery_capacity = db.Column(db.String(40))
    battery_removable = db.Column(db.Boolean)
    fingerprint_sensor = db.Column(db.Boolean)
    water_resistant = db.Column(db.Boolean)



class Userfilter(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(60), db.ForeignKey('user.id'))
    date_made = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    ordered = db.Column(db.String(60), db.ForeignKey('orders.id'))
    brand = db.Column(db.String(40))
    year = db.Column(db.String(10))
    description = db.Column(db.Text(1000)) 
    phone_image_front = db.Column(db.Text(1024))
    phone_image_back = db.Column(db.Text(1024))
    phone_image_side = db.Column(db.Text(1024))
    name = db.Column(db.String(300))
    price = db.Column(db.Float)
    rating = db.Column(db.Integer)
    features = db.Column(db.PickleType, default={})

    new = db.Column(db.Boolean)
    network = db.Column(db.String(40))
    sim_card_slot_size = db.Column(db.String(40))
    sim_slot_count = db.Column(db.Integer)
    body_form_factor = db.Column(db.String(40)) #bar flip slider
    body_color = db.Column(db.String(40))
    os = db.Column(db.String(40))
    ram = db.Column(db.Integer)
    storage = db.Column(db.Integer)
    display_type = db.Column(db.String(40))
    display_resolution = db.Column(db.String(40))
    camera_resolution = db.Column(db.String(40))
    wlan = db.Column(db.Boolean)
    bluetooth = db.Column(db.Boolean)
    gps = db.Column(db.Boolean)
    fm_radio = db.Column(db.Boolean)
    connector_type = db.Column(db.Boolean) #eg. usb_type_c
    battery_capacity = db.Column(db.String(40))
    battery_removable = db.Column(db.Boolean)
    fingerprint_sensor = db.Column(db.Boolean)
    water_resistant = db.Column(db.Boolean)




# class Phones2(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     brand
#     year
#     color 
#     storage
#     display_size
#     aspect_ratio
#     network
#     sim_card_size
#     bluetooth = db.Column(db.Boolean)
#     wifi = db.Column(db.Boolean)
#     nfc = db.Column(db.Boolean)
#     infrared = db.Column(db.Boolean)
#     usb = db.Column(db.Boolean)
#     brand = db.Column(db.String(40))
#     year = db.Column(db.String(10))
#     availability = db.Column(db.String(40))
#     price = db.Column(db.String(20))
#     network_2g = db.Column(db.String(40))
#     network_3g = db.Column(db.String(40))
#     network_4g = db.Column(db.String(40))
#     network_5g = db.Column(db.String(40))
#     sim_size = db.Column(db.String(40))
#     sim_multiple = db.Column(db.String(40))
#     body_form_factor = db.Column(db.String(40))
#     body_keyboard = db.Column(db.String(40))
#     body_height = db.Column(db.String(40))
#     body_width = db.Column(db.String(40))
#     body_weight = db.Column(db.String(40))
#     body_thickness = db.Column(db.String(40))
#     body_ip_certificate = db.Column(db.String(40))
#     body_color = db.Column(db.String(40))
#     body_back_material = db.Column(db.String(40))
#     body_frame_material = db.Column(db.String(40))
#     os = db.Column(db.String(40))
#     os_version = db.Column(db.String(40))
#     cpu_freq = db.Column(db.String(40))
#     cpu_cores = db.Column(db.Integer)
#     chipset = db.Column(db.String(40))
#     ram = db.Column(db.String(40))
#     storage = db.Column(db.String(40))
#     card_slot = db.Column(db.String(40))
#     display_resolution = db.Column(db.String(40))
#     display_size = db.Column(db.String(40))
#     display_density = db.Column(db.String(40))
#     display_technology = db.Column(db.String(40))
#     display_notch = db.Column(db.String(40))
#     display_high_refresh_rate = db.Column(db.Boolean)
#     display_hdr = db.Column(db.Boolean)
#     main_camera_resolution = db.Column(db.String(40))
#     main_camera_f_number = db.Column(db.String(40))
#     main_camera_cameras = db.Column(db.String(40))
#     main_camera_ois = db.Column(db.Boolean)
#     main_camera_telephoto = db.Column(db.Boolean)
#     main_camera_ultrawide = db.Column(db.Boolean)
#     main_camera_flash = db.Column(db.Boolean)
#     main_camera_video = db.Column(db.String(40))
#     selfie_camera_resolution = db.Column(db.String(40))
#     selfie_camera_dual_camera = db.Column(db.Boolean)
#     selfie_camera_ois = db.Column(db.Boolean)
#     selfie_camera_front_flask = db.Column(db.Boolean)
#     selfie_camera_pop_up_camera = db.Column(db.Boolean)
#     selfie_camera_under_display = db.Column(db.Boolean)
#     sensor_accelerometer = db.Column(db.Boolean)
#     sensor_compass = db.Column(db.Boolean)
#     sensor_gyro = db.Column(db.Boolean)
#     sensor_compass = db.Column(db.Boolean)
#     sensor_proximity = db.Column(db.Boolean)
#     sensor_heart_rate = db.Column(db.Boolean)
#     sensor_fingerprint = db.Column(db.String(40))
#     wlan = db.Column(db.String(40))
#     bluetooth = db.Column(db.String(40))
#     gps = db.Column(db.Boolean)
#     nfc = db.Column(db.Boolean)
#     infrared = db.Column(db.Boolean)
#     fm_radio = db.Column(db.Boolean)
#     usb_type_c = db.Column(db.Boolean)
#     battery_capacity = db.Column(db.String(40))
#     battery_removable = db.Column(db.String(40))
#     charging_wired = db.Column(db.String(40))
#     charging_wireless = db.Column(db.String(40))
#     misc_free_text = db.Column(db.String(40))
#     misc_order = db.Column(db.String(40))
#     misc_reviewed_only = db.Column(db.Boolean)
#     new = db.Column(db.Boolean)
#     description = db.Column(db.Text(1000)) 
#     name = db.Column(db.String(300))
#     price = db.Column(db.Float)
#     rating = db.Column(db.Integer)
