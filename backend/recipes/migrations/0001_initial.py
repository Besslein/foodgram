# Generated by Django 4.2.16 on 2024-10-08 11:53

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Избранное',
                'verbose_name_plural': 'Избранное',
                'ordering': ('id',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Ингредиент: обязательное поле', max_length=128, verbose_name='Ингредиент')),
                ('measurement_unit', models.CharField(help_text='Единица измерения: обязательное поле', max_length=64, verbose_name='Единица измерения')),
            ],
            options={
                'verbose_name': 'Ингредиент',
                'verbose_name_plural': 'Ингредиенты',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(help_text='Картинка: обязательное поле', upload_to='recipes/images/', verbose_name='Фото готового блюда')),
                ('name', models.CharField(help_text='Название рецепта: обязательное поле', max_length=256, verbose_name='Название рецепта')),
                ('text', models.TextField(help_text='Описание рецепта: обязательное поле', verbose_name='Описание рецепта')),
                ('cooking_time', models.PositiveSmallIntegerField(help_text='Время приготовления: обязательное поле', validators=[django.core.validators.MinValueValidator(1, message='Минимальное время - 1 мин.')], verbose_name='Время приготовления (в минутах)')),
                ('short_url_code', models.CharField(editable=False, max_length=5, unique=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recipes', to=settings.AUTH_USER_MODEL, verbose_name='Автор рецепта')),
            ],
            options={
                'verbose_name': 'Рецепт',
                'verbose_name_plural': 'Рецепты',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True, verbose_name='Тег рецепта')),
                ('slug', models.SlugField(max_length=32, unique=True, validators=[django.core.validators.RegexValidator(message='Неверный формат', regex='^[-a-zA-Z0-9_]+$')], verbose_name='Слаг')),
            ],
            options={
                'verbose_name': 'Тег',
                'verbose_name_plural': 'Теги',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='ShoppingList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s', to='recipes.recipe', verbose_name='Рецепт')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Список покупок',
                'verbose_name_plural': 'Списки покупок',
                'ordering': ('id',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RecipeIngredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(1, message='Минимальное количество любого ингредиента в рецепте:  1 ед.')], verbose_name='Количество')),
                ('ingredient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='recipes.ingredient', verbose_name='Ингредиент')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ingredients', to='recipes.recipe', verbose_name='Рецепт')),
            ],
            options={
                'verbose_name': 'Количество ингредиента в рецепте',
                'verbose_name_plural': 'Количество ингредиента в рецепте',
                'ordering': ('id',),
            },
        ),
        migrations.AddField(
            model_name='recipe',
            name='tags',
            field=models.ManyToManyField(help_text='Теги: обязательное поле', to='recipes.tag', verbose_name='Список id тегов'),
        ),
        migrations.AddConstraint(
            model_name='ingredient',
            constraint=models.UniqueConstraint(fields=('name', 'measurement_unit'), name='ingredient_measurement_unit_pair_unique'),
        ),
        migrations.AddField(
            model_name='favorite',
            name='recipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s', to='recipes.recipe', verbose_name='Рецепт'),
        ),
        migrations.AddField(
            model_name='favorite',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
        migrations.AddConstraint(
            model_name='shoppinglist',
            constraint=models.UniqueConstraint(fields=('user', 'recipe'), name='shoppinglist_user_recipe_unique'),
        ),
        migrations.AddConstraint(
            model_name='recipeingredient',
            constraint=models.UniqueConstraint(fields=('recipe', 'ingredient'), name='recipe_ingredient_pair_unique'),
        ),
        migrations.AddConstraint(
            model_name='favorite',
            constraint=models.UniqueConstraint(fields=('user', 'recipe'), name='favorite_user_recipe_unique'),
        ),
    ]
