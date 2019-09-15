# Generated by Django 2.2.5 on 2019-09-13 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0005_auto_20190912_1647'),
    ]

    operations = [
        migrations.AlterField(
            model_name='survey',
            name='a5',
            field=models.TextField(blank=True, choices=[('Saidapet', 'Saidapet'), ('Perambur', 'Perambur'), ('Thiru Vi Ka Nagar (SC)', 'Thiru Vi Ka Nagar (SC)'), ('Harbour', 'Harbour'), ('Vellore', 'Vellore'), ('Tiruppatur', 'Tiruppatur'), ('Arkonam (SC)', 'Arkonam (SC)'), ('Gudiyattam (SC)', 'Gudiyattam (SC)'), ('Omalur', 'Omalur'), ('Mettur', 'Mettur'), ('Yarcard (ST)', 'Yarcard (ST)'), ('Sankari', 'Sankari'), ('Nagapptinam', 'Nagapptinam'), ('Kilvelur (SC)', 'Kilvelur (SC)'), ('Myladuthurai', 'Myladuthurai'), ('Sirkalzi (SC)', 'Sirkalzi (SC)'), ('Sankarankovil (SC)', 'Sankarankovil (SC)'), ('Tenkasi', 'Tenkasi'), ('Alangulam', 'Alangulam'), ('Palayamkottai', 'Palayamkottai'), ('Karaikudi', 'Karaikudi'), ('Tiruppattur', 'Tiruppattur'), ('Sivaganga', 'Sivaganga'), ('Manamadurai', 'Manamadurai')], null=True, verbose_name='a5'),
        ),
        migrations.AlterField(
            model_name='survey',
            name='c3',
            field=models.CharField(blank=True, choices=[('0-Never', '0-Never'), ('1-Yes, application in progress', '1-Yes, application in progress'), ('2-Yes, currently enrolled', '2-Yes, currently enrolled')], max_length=128, null=True, verbose_name='c3'),
        ),
    ]