from api import PetFriends
import os

pf = PetFriends()

#1
from settings import unvalid_email, unvalid_password
def test_get_api_key_for_unvalid_user(email=unvalid_email, password=unvalid_password):
    """ Проверяем что запрос api ключа c невалидными данными возвращает статус 403 (запрет) """
    status, result = pf.get_api_key(email, password)
    # Сверяем полученные данные с нашими ожиданиями
    assert status == 403

#2
from settings import valid_email, valid_password
def test_add_new_pet_with_long_name(name='111111111111111111111111111111111111', animal_type='Персидская',
                                     age='15', pet_photo='images/pusya.jpg'):
    """Проверяем что произойдет если добавить питомца с длинным именем"""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    assert status == 200
    assert result['name'] == name

#3
def test_add_new_pet_with_no_name(name='', animal_type='Персидская',
                                     age='15', pet_photo='images/pusya.jpg'):
    """Проверяем что произойдет если добавить питомца без имени"""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    assert status == 200
    assert result['name'] == name

#4
def test_add_new_pet_with_different_language_name(name='Simba-Симба', animal_type='Персидская',
                                     age='15', pet_photo='images/pusya.jpg'):
    """Проверяем что произойдет если добавить питомца с разной кодировкой"""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    assert status == 200
    assert result['name'] == name

#5
def test_add_new_pet_with_small_photo(name='Simba-Симба', animal_type='Персидская',
                                     age='15', pet_photo='images/pusya_1.jpg'):
    """Проверяем что произойдет если добавить питомца с фото 1 кб"""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    assert status == 200
    assert result['name'] == name

#6
def test_add_new_pet_with_big_photo(name='Simba-Симба', animal_type='Персидская',
                                     age='15', pet_photo='images/pusya_2.jpg'):
    """Проверяем что произойдет если добавить питомца с фото более 3000 кб"""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    assert status == 200
    assert result['name'] == name

#7
def test_add_new_pet_with_png_photo(name='sfsfsfs', animal_type='Персидская',
                                     age='15', pet_photo='images/pusya.png'):
    """Проверяем что произойдет если добавить питомца с фото png формата"""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    assert status == 200
    assert result['name'] == name
    #failed, тк в библиотеке прописан только jpg формат

#8
def test_add_new_pet_with_photo_of_wrong_format(name='Simba-Симба', animal_type='Персидская',
                                     age='15', pet_photo='images/pusya_3.txt'):
    """Проверяем что произойдет если добавить питомца с фото текстового формата"""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    #Должен выдать ошибку сервера
    assert status == 500

#9
def test_update_self_pet_info_with_literal_age(name='Муха', animal_type='Кошка', age='два'):
    """Проверяем возможность обновления информации о питомце, в поле возраста - буквенное значение"""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)
    assert status == 200
    assert result['name'] == name

#10
def test_update_self_pet_info_with_no_data(name='', animal_type='', age=''):
    """Проверяем возможность обновления информации о питомце с пустыми значениями"""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)
    assert status == 200
    assert result['name'] == name