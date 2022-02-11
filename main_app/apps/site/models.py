import uuid
from typing import Optional, List

from pydantic import UUID4, BaseModel, Field

from database.main_db import db_provider

from config import settings

# site models changes here

class SocialContact(BaseModel):
    value: str = ""
    label: str = ""
    link: str = ""

    @staticmethod
    def get_defaults() -> list:
        telegram_link = "https://fast-code.ru/"
        viber_link = "https://fast-code.ru/"
        whatsapp_link = "https://fast-code.ru/"
        vk_link = "https://fast-code.ru/"
        inst_link = "https://fast-code.ru/"
        telegram = SocialContact(
            value = "telegram",
            label = "Telegram",
            link = telegram_link
        )
        viber = SocialContact(
            value = "viber",
            label = "Viber",
            link = viber_link
        )
        whatsapp = SocialContact(
            value = "whatsapp",
            label = "Whatsapp",
            link = whatsapp_link
        )
        vk = SocialContact(
            value = "vk",
            label = "Vk",
            link = vk_link
        )
        inst = SocialContact(
            value = "inst",
            label = "Instagram",
            link = inst_link
        )
        return [telegram, viber, whatsapp, vk, inst]

class CommonInfo(BaseModel):
    location_address: str = ""
    delivery_phone: str = ""
    delivery_phone_display: str = ""
    main_logo_link: str = ""
    map_delivery_locaition_link: str = ""
    socials: List[SocialContact] = []

    @staticmethod
    def get_default():
        info = CommonInfo(
            location_address = "Здесь будет адрес доставки",
            delivery_phone = "+79781111111",
            delivery_phone_display = "7 978 111 11 11",
            main_logo_link = settings.base_static_url + "logo_variant.png",
            map_delivery_location_link = "https://yandex.ru/map-widget/v1/?um=constructor%3A9b116676061cfe4fdf22efc726567c5f21c243f18367e2b8a207accdae7e4786&amp;source=constructor",
            socials = SocialContact.get_defaults()
        )
        return info

    class Config:
        allow_population_by_field_name = True

class ColorARGB(BaseModel):
    a: int = 255
    r: int = 255
    g: int = 255
    b: int = 255

class PickupAddress(BaseModel):
    id: UUID4 = Field(default_factory=uuid.uuid4, alias="_id")
    name: str
    info: str = ""

    def save_db(self):
        db_provider.pickup_addresses_db.insert_one(
            self.dict(by_alias=True)
        )

class StockItem(BaseModel):
    id: UUID4 = Field(default_factory=uuid.uuid4, alias="_id")
    title: str
    description: Optional[str]
    imgsrc: List[str] = []

    def save_db(self):
        db_provider.stocks_db.insert_one(
            self.dict(by_alias=True)
        )

class MenuLink(BaseModel):
    id: UUID4 = Field(default_factory=uuid.uuid4, alias="_id")
    link_name: Optional[str]
    link_path: Optional[str] 
    display_order: Optional[int] = 0


class MainSliderItem(BaseModel):
    id: UUID4 = Field(default_factory=uuid.uuid4, alias="_id")
    link_path: Optional[str] 
    display_order: Optional[int] = 0
    imgsrc: str

class RequestCall(BaseModel):
    name: str = ""
    phone: str = ""
    phone_mask: str = ""
