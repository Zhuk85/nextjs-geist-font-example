# Generated by Django 5.2.3 on 2025-06-14 03:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("categories", "0001_initial"),
        ("cities", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="StickerLike",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "verbose_name": "Лайк стикера",
                "verbose_name_plural": "Лайки стикеров",
            },
        ),
        migrations.CreateModel(
            name="Sticker",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=200, verbose_name="Название")),
                ("description", models.TextField(blank=True, verbose_name="Описание")),
                (
                    "image",
                    models.ImageField(
                        upload_to="stickers/", verbose_name="Изображение"
                    ),
                ),
                (
                    "price",
                    models.DecimalField(
                        decimal_places=2, default=0, max_digits=10, verbose_name="Цена"
                    ),
                ),
                (
                    "is_available",
                    models.BooleanField(default=True, verbose_name="Доступен"),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Создан"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Обновлен"),
                ),
                (
                    "views_count",
                    models.PositiveIntegerField(default=0, verbose_name="Просмотры"),
                ),
                (
                    "likes_count",
                    models.PositiveIntegerField(default=0, verbose_name="Лайки"),
                ),
                (
                    "approval_status",
                    models.CharField(
                        choices=[
                            ("pending", "На модерации"),
                            ("approved", "Одобрен"),
                            ("rejected", "Отклонен"),
                        ],
                        default="pending",
                        max_length=20,
                        verbose_name="Статус модерации",
                    ),
                ),
                (
                    "category",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="categories.category",
                    ),
                ),
                (
                    "city",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="cities.city",
                    ),
                ),
            ],
            options={
                "verbose_name": "Стикер",
                "verbose_name_plural": "Стикеры",
                "ordering": ["-created_at"],
            },
        ),
    ]
