from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List

db = SQLAlchemy()

class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    username: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    firstname: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    lastname: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)

    favorite_characters: Mapped[List["FavoriteCharacter"]] = relationship(back_populates="user")
    favorite_planets: Mapped[List["FavoritePlanet"]] = relationship(back_populates="user")

class Character(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    height: Mapped[int] = mapped_column(primary_key=True)
    gender: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    eyes_color: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)

class Planet(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    diameter: Mapped[int] = mapped_column(primary_key=True)
    climate: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    terrain: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)

class FavoriteCharacter(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    character_id: Mapped[int] = mapped_column(primary_key=True)

    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    user: Mapped["User"] = relationship(back_populates="favorite_character")


class FavoritePlanet(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    planet_id: Mapped[int] = mapped_column(primary_key=True)

    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    user: Mapped["User"] = relationship(back_populates="favorite_planet")


    	

    		

    			

		
