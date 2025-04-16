from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean,ForeignKey,Table,Column
from sqlalchemy.orm import Mapped, mapped_column,relationship
from datetime import datetime,timezone

db = SQLAlchemy()

association_usuario_personaje = Table(
    "usuario_personaje", db.metadata,
    Column("usuario_id", ForeignKey("usuarios.id"), primary_key=True),
    Column("personaje_id", ForeignKey("personajes.id"), primary_key=True)
)
association_usuario_planeta = Table(
    "usuario_planeta", db.metadata,
    Column("usuario_id", ForeignKey("usuarios.id"), primary_key=True),
    Column("planeta_id", ForeignKey("planetas.id"), primary_key=True)
)
association_usuario_nave = Table(
    "usuario_nave", db.metadata,
    Column("usuario_id", ForeignKey("usuarios.id"), primary_key=True),
    Column("nave_id", ForeignKey("naves.id"), primary_key=True)
)

class User(db.Model):
    __tablename__ = "usuarios"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    name: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean(), nullable=False)
    created: Mapped[datetime] = mapped_column(default=lambda: datetime.now(timezone.utc))

    personajes_favoritos:Mapped[list["Personaje"]]=relationship(secondary=association_usuario_personaje,back_populates="favotiro_por")

    planetas_favoritos:Mapped[list["Planeta"]]=relationship(secondary=association_usuario_planeta,back_populates="favotiro_por")
    naves_favoritos:Mapped[list["Nave"]]=relationship(secondary=association_usuario_nave,back_populates="favotiro_por")

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

class Personaje(db.Model):
    __tablename__="personajes"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100),  nullable=False)
    birth_year:Mapped[str] =mapped_column(String(20), nullable=False)
    gender:Mapped[str] =mapped_column(String(30), nullable=False)
    height:Mapped[str] =mapped_column(String(30), nullable=False)
    image_url:Mapped[str] =mapped_column(nullable=False)

    favotiro_por:Mapped[list["User"]]=relationship(secondary=association_usuario_personaje,back_populates="personajes_favoritos")
    
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            # do not serialize the password, its a security breach
        }
    

class Planeta(db.Model):
    __tablename__="planetas"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    climate: Mapped[str] = mapped_column(String(20), nullable=False)
    diameter: Mapped[str] = mapped_column(String(20), nullable=False)
    gravity: Mapped[str] = mapped_column(String(10), nullable=False)
    orbital_period: Mapped[str] = mapped_column(String(20), nullable=False)

    favotiro_por:Mapped[list["User"]]=relationship(secondary=association_usuario_planeta,back_populates="planetas_favoritos")
    
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            # do not serialize the password, its a security breach
        }

class Nave(db.Model):
    __tablename__="naves"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)

    favotiro_por:Mapped[list["User"]]=relationship(secondary=association_usuario_nave,back_populates="naves_favoritos")
    
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            # do not serialize the password, its a security breach
        }