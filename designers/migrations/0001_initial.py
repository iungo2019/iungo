# Generated by Django 3.1.2 on 2020-10-27 10:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=50)),
                ('image', models.ImageField(null=True, upload_to='category/')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Designers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('projects_completed', models.PositiveIntegerField()),
                ('projects_ongoing', models.PositiveIntegerField()),
                ('happy_customers', models.PositiveIntegerField()),
                ('max_budget', models.PositiveIntegerField()),
                ('min_budget', models.PositiveIntegerField()),
                ('profile_image', models.ImageField(null=True, upload_to='profile/')),
                ('banner_image', models.ImageField(null=True, upload_to='banner/')),
                ('pincode', models.PositiveIntegerField(null=True)),
                ('city', models.CharField(max_length=50, null=True)),
                ('description', models.TextField()),
                ('short_description', models.TextField(null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('phone_number', models.CharField(max_length=15, null=True)),
                ('alternate_phone_number', models.CharField(max_length=15, null=True)),
                ('website', models.URLField(null=True)),
                ('company_name', models.CharField(max_length=50, null=True)),
                ('address', models.TextField(null=True)),
                ('facebook_link', models.URLField(null=True)),
                ('instagram_link', models.URLField(null=True)),
                ('youtube_link', models.URLField(null=True)),
                ('experience', models.PositiveIntegerField(null=True)),
                ('Project_Consultation', models.CharField(choices=[('Available', 'availbale'), ('Not available ', 'Not available')], max_length=50, null=True)),
                ('Project_Design', models.CharField(choices=[('Available', 'availbale'), ('Not available ', 'Not available')], max_length=50, null=True)),
                ('Production', models.CharField(choices=[('Available', 'availbale'), ('Not available ', 'Not available')], max_length=50, null=True)),
                ('Furniture_design', models.CharField(choices=[('Available', 'availbale'), ('Not available ', 'Not available')], max_length=50, null=True)),
                ('Design_Consultancy', models.CharField(choices=[('Available', 'availbale'), ('Not available ', 'Not available')], max_length=50, null=True)),
                ('Home_Advising', models.CharField(choices=[('Available', 'availbale'), ('Not available ', 'Not available')], max_length=50, null=True)),
                ('Remodeling', models.CharField(choices=[('Available', 'availbale'), ('Not available ', 'Not available')], max_length=50, null=True)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='designers.category')),
            ],
            options={
                'verbose_name': 'Designer',
                'verbose_name_plural': 'Designers',
            },
        ),
        migrations.CreateModel(
            name='Reserve',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=15, null=True)),
                ('pincode', models.CharField(max_length=15, null=True)),
                ('Requirements', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Style',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('style_name', models.CharField(max_length=50)),
                ('image', models.ImageField(null=True, upload_to='Style/')),
            ],
            options={
                'verbose_name': 'Style',
                'verbose_name_plural': 'Styles',
            },
        ),
        migrations.CreateModel(
            name='ProjectImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='projectimages/')),
                ('designer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='designers.designers')),
            ],
            options={
                'verbose_name': 'Project Image',
                'verbose_name_plural': 'Project Images',
            },
        ),
        migrations.AddField(
            model_name='designers',
            name='style',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='designers.style'),
        ),
        migrations.CreateModel(
            name='DesignerOffice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='DesignerOffice/')),
                ('designer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='designers.designers')),
            ],
            options={
                'verbose_name': 'DesignerOffice',
                'verbose_name_plural': 'DesignerOffices',
            },
        ),
        migrations.CreateModel(
            name='Banks_approved',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('banks_approved', models.CharField(choices=[('Axis Bank', 'Axis Bank'), ('Bandhan Bank', 'Bandhan Bank'), ('CSB Bank', 'CSB Bank'), ('City Union Bank', 'City Union Bank'), ('DCB Bank', 'DCB Bank'), ('Dhanlaxmi Bank', 'Dhanlaxmi Bank'), ('Federal Bank', 'Federal Bank'), ('HDFC Bank', 'HDFC Bank'), ('ICICI Bank', 'ICICI Bank'), ('IDBI Bank', 'IDBI Bank'), ('IDFC First Bank', 'IDFC First Bank'), ('IndusInd Bank', 'IndusInd Bank'), ('Karnataka Bank', 'Ready to move'), ('Karur Vysya Bank', 'Karur Vysya Bank'), ('Kotak Mahindra Bank', 'Kotak Mahindra Bank'), ('Lakshmi Vilas Bank', 'Lakshmi Vilas Bank'), ('Nainital Bank', 'Nainital Bank'), ('RBL Bank', 'RBL Bank'), ('South Indian Bank', 'South Indian Bank'), ('Tamilnad Mercantile Bank Limited', 'Tamilnad Mercantile Bank Limited'), ('Yes Bank', 'Yes Bank')], max_length=50, null=True)),
                ('loan_details', models.TextField()),
                ('designer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='designers.designers')),
            ],
            options={
                'verbose_name': 'Bank approved',
                'verbose_name_plural': 'Banks approved',
            },
        ),
    ]