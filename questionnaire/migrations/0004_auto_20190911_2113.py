# Generated by Django 2.2.5 on 2019-09-11 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0003_auto_20190911_1736'),
    ]

    operations = [
        migrations.AddField(
            model_name='survey',
            name='a3_code',
            field=models.IntegerField(choices=[(603, 603), (605, 605), (608, 608), (618, 618), (622, 622), (628, 628)], default=603, verbose_name='a3_code'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='survey',
            name='a5_code',
            field=models.TextField(blank=True, choices=[(23, 23), (12, 12), (15, 15), (18, 18), (43, 43), (50, 50), (38, 38), (46, 46), (83, 83), (84, 84), (85, 85), (87, 87), (160, 160), (161, 161), (163, 163), (164, 164), (219, 219), (222, 222), (223, 223), (226, 226), (184, 184), (185, 185), (186, 186), (187, 187)], null=True, verbose_name='a5'),
        ),
        migrations.AlterField(
            model_name='survey',
            name='a3',
            field=models.TextField(choices=[('Chennai', 'Chennai'), ('Vellore', 'Vellore'), ('Salem', 'Salem'), ('Nagapattinam', 'Nagapattinam'), ('Thirunelveli', 'Thirunelveli'), ('Sivagangai', 'Sivagangai')], verbose_name='a3'),
        ),
        migrations.AlterField(
            model_name='survey',
            name='a5',
            field=models.TextField(blank=True, choices=[('Saidapet', 'Saidapet'), ('Perambur', 'Perambur'), ('Thiru Vi Ka Nagar (SC)', 'Thiru Vi Ka Nagar (SC)'), ('Harbour', 'Harbour'), ('Vellore', 'Vellore'), ('Tiruppatur', 'Tiruppatur'), ('Arkonam (SC)', 'Arkonam (SC)'), ('Gudiyattam (SC)', 'Gudiyattam (SC)'), ('Omalur', 'Omalur'), ('Mettur', 'Mettur'), ('Yarcard (ST)', 'Yarcard (ST)'), ('Sankari', 'Sankari'), ('Nagapptinam', 'Nagapptinam'), ('Kilvelur (SC)', 'Kilvelur (SC)'), ('Myladuthurai', 'Myladuthurai'), ('Sirkalzi (SC)', 'Sirkalzi (SC)'), ('Sankarankovil (SC)', 'Sankarankovil (SC)'), ('Tenkasi', 'Tenkasi'), ('Palayamkottai', 'Palayamkottai'), ('Karaikudi', 'Karaikudi'), ('Tiruppattur', 'Tiruppattur'), ('Sivaganga', 'Sivaganga'), ('Manamadurai', 'Manamadurai')], null=True, verbose_name='a5'),
        ),
    ]