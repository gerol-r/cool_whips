# main_app/migrations/0006_update_car_image_urls.py
from django.db import migrations

def update_car_image_urls(apps, schema_editor):
    Car = apps.get_model('main_app', 'Car')
    
    # Update image URLs for specific cars
    # Adjust URLs to match correct image file paths
    car_updates = [
        # Format: (make, model, trim_level, new_image_url)
        ("Bugatti", "Chiron", "Super Sport 300+", "/static/images/cars/bugatti_chiron.jpg"),
        ("McLaren", "Senna", "Coupe", "/static/images/cars/mclaren_senna.jpg"),
        ("Mercedes-Maybach", "G 650", "Landaulet", "/static/images/cars/mercedes_maybach_g650.jpg"),
        ("Porsche", "911", "GT2 RS", "/static/images/cars/porsche_gt2_rs.jpg"),
        ("Rezvani", "Vengeance", "Military Executive", "/static/images/cars/rezvani_vengeance.jpg"),
        ("Ferrari", "812", "Competizione", "/static/images/cars/ferari_812.jpg"),
        ("Lamborghini", "Aventador", "SVJ", "/static/images/cars/lamborghini_aventador.jpg"),
        ("BMW", "M4", "Competition", "/static/images/cars/bmw_m4.jpg"),
        ("Ford", "F-150", "Raptor R", "/static/images/cars/ford_f150.jpg"),
        ("Porsche", "Cayman", "S", "/static/images/cars/porsche_cayman.jpg"),
        ("Mercedes-AMG", "C 63", "S", "/static/images/cars/mercedes_amg_c63.jpg"),
        ("Ford", "Mustang", "Dark Horse", "/static/images/cars/ford_mustang.jpg"),
        ("Toyota", "GR Supra", "3.0", "/static/images/cars/toyota_supra.jpg"),
        ("Jeep", "Wrangler", "Rubicon", "/static/images/cars/jeep_wrangler.jpg"),
        ("Lexus", "RC F", None, "/static/images/cars/lexus_rcf.jpg"),
    ]
    
    for make, model, trim_level, image_url in car_updates:
        try:
            if trim_level:
                car = Car.objects.get(make=make, model=model, trim_level=trim_level)
            else:
                car = Car.objects.get(make=make, model=model, trim_level__isnull=True)
            car.image_url = image_url
            car.save()
            print(f"Updated {make} {model} image URL")
        except Car.DoesNotExist:
            print(f"Car not found: {make} {model} {trim_level}")
        except Car.MultipleObjectsReturned:
            print(f"Multiple cars found for: {make} {model} {trim_level}")

class Migration(migrations.Migration):
    dependencies = [
        ('main_app', '0005_auto_20250616_1959'), 
    ]
    
    operations = [
        migrations.RunPython(update_car_image_urls),
    ]