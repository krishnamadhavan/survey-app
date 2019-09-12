from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _
from django.db import models

User = get_user_model()


bool_choices = (('0-No', '0-No'), ('1-Yes', '1-Yes'))
null_boolean_choices = (('0-No', '0-No'), ('1-Yes', '1-Yes'), ('9-Don\'t know', '9-Don\'t know'))
somewhat_choices = (('0-No', '0-No'), ('1-Somewhat', '1-Somewhat'), ('2-Yes', '2-Yes'))


class Survey(models.Model):
    a1_choices = (('1-Received', '1-Received'), ('0-Not received', '0-Not received'))
    a3_choices = (('Chennai', 'Chennai'), ('Vellore', 'Vellore'), ('Salem', 'Salem'), ('Nagapattinam', 'Nagapattinam'),
                  ('Thirunelveli', 'Thirunelveli'), ('Sivagangai', 'Sivagangai'))
    a3_code_choices = ((603, 603), (605, 605), (608, 608), (618, 618), (622, 622), (628, 628))
    a4_choices = (('1-Urban', '1-Urban'), ('0-Rural', '0-Rural'))
    a5_choices = (('Saidapet', 'Saidapet'), ('Perambur', 'Perambur'), ('Thiru Vi Ka Nagar (SC)',
                                                                       'Thiru Vi Ka Nagar (SC)'),
                  ('Harbour', 'Harbour'), ('Vellore', 'Vellore'), ('Tiruppatur', 'Tiruppatur'),
                  ('Arkonam (SC)', 'Arkonam (SC)'), ('Gudiyattam (SC)', 'Gudiyattam (SC)'), ('Omalur', 'Omalur'),
                  ('Mettur', 'Mettur'), ('Yarcard (ST)', 'Yarcard (ST)'), ('Sankari', 'Sankari'),
                  ('Nagapptinam', 'Nagapptinam'), ('Kilvelur (SC)', 'Kilvelur (SC)'), ('Myladuthurai', 'Myladuthurai'),
                  ('Sirkalzi (SC)', 'Sirkalzi (SC)'), ('Sankarankovil (SC)', 'Sankarankovil (SC)'),
                  ('Tenkasi', 'Tenkasi'), ('Palayamkottai', 'Palayamkottai'), ('Karaikudi', 'Karaikudi'),
                  ('Tiruppattur', 'Tiruppattur'), ('Sivaganga', 'Sivaganga'), ('Manamadurai', 'Manamadurai')
                  )
    a5_code_choices = ((23, 23), (12, 12), (15, 15), (18, 18), (43, 43), (50, 50), (38, 38), (46, 46), (83, 83),
                       (84, 84), (85, 85), (87, 87), (160, 160), (161, 161), (163, 163), (164, 164), (219, 219),
                       (222, 222), (223, 223), (226, 226), (184, 184), (185, 185), (186, 186), (187, 187))
    a12_choices = (('1-Completed', '1-Completed'), ('2-Entire HH absent for a long time',
                                                    '2-Entire HH absent for a long time'),
                   ('3-Postponed', '3-Postponed'), ('4-Refused (Pl. specify reasons)', 'Refused (Pl. specify reasons)'),
                   ('5-HH/dwelling vacant', '5-HH/dwelling vacant'), ('6-Address of HH/dwelling not found',
                                                                      '6-Address of HH/dwelling not found')
                   )
    c3_choices = (('0-Never', '0-Never'), ('1-Yes, application in progress', '1-Yes, application in progress'),
                  ('2-Yes, currently enrolled', '2-Yes, currently enrolled')
                  )
    c5_choices = (('0-Incorrect polling station', '0-Incorrect polling station'),
                  ('1-Correct polling station', '1-Correct polling station'))
    c6_choices = (('1-During a special enrollment drive', '1-During a special enrollment drive'),
                  ('01-A Booth Level Officer had visited residence', '01-A Booth Level Officer had visited residence'),
                  ('02-Went to the local voter enrollment center', '02-Went to the local voter enrollment center'),
                  ('03-Went to the State Election Office', '03-Went to the State Election Office'),
                  ('04-Online/NVSP', '04-Online/NVSP'), ('05-With help from political parties',
                                                         '05-With help from political parties'),
                  ('06-With help from CSO/Association/Individual', '06-With help from CSO/Association/Individual'),
                  ('07-Don\'t know', '07-Don\'t know'), ('99-Others(please specify)', '99-Others(please specify)')
                  )
    c7_choices = (('1-Easy', '1-Easy'), ('2-Neither easy nor difficult', '2-Neither easy nor difficult'),
                  ('3-Difficult', '3-Difficult'), ('9-Don\'t know', '9-Don\'t know'))
    c9_choices = (('01-Got the acknowledgment', '01-Got the acknowledgment'),
                  ('02-An election official has visited me', '02-An election official has visited me'),
                  ('03-Waiting for acknowledgment', '03-Waiting for acknowledgment'),
                  ('04-Proof of address rejected/insufficient', '04-Proof of address rejected/insufficient'),
                  ('05-Proof of age/other documents rejected/insufficient',
                   '05-Proof of age/other documents rejected/insufficient'),
                  ('99-Others(please specify)', '99-Others(please specify)')
                  )
    c10_choices = (('01-I don\'t know the procedure', '01-I don\'t know the procedure'),
                   ('02-The procedure is very cumbersome', '02-The procedure is very cumbersome'),
                   ('03-Do not have any proof of residence', '03-Do not have any proof of residence'),
                   ('04-I am not interested', '04-I am not interested'),
                   ('99-Others(please specify)', '99-Others(please specify)')
                   )
    d2_choices = (('01-My vote matters', '01-My vote matters'), ('02-Voting is my right', '02-Voting is my right'),
                  ('03-Voting is my duty', '03-Voting is my duty'),
                  ('04-Because of enabling environment (free and fair) created by Election Commission',
                   '04-Because of enabling environment (free and fair) created by Election Commission'),
                  ('05-Because of accessible polling station', '05-Because of accessible polling station'),
                  ('06-I got registered in electoral roll', '06-I got registered in electoral roll'),
                  ('07-I got voter slip', '07-I got voter slip'), ('08-Candidate was good', '08-Candidate was good'),
                  ('09-I voted for a political party', '09-I voted for a political party'),
                  ('10-Cast vote due to threat or coercion', '10-Cast vote due to threat or coercion'),
                  ('12-My family asked me to', '12-My family asked me to'), ('13-My friends asked me to',
                                                                             '13-My friends asked me to'),
                  ('14-I had the option of NOTA', '14-I had the option of NOTA')
                  )
    d5_choices = (('01-Long queue', '01-Long queue'),
                  ('02-No separate queue for senior citizen', '02-No separate queue for senior citizen'),
                  ('03-Lack of facilities including drinking water toilet and ramp',
                   '03-Lack of facilities including drinking water toilet and ramp'),
                  ('04-Coercion/ threat by political party', '04-Coercion/ threat by political party'),
                  ('05-Difficulties in locating my polling station', '05-Difficulties in locating my polling station'),
                  ('06-Difficulties in voting in absence of voter slip',
                   '06-Difficulties in voting in absence of voter slip'),
                  ('07-No guidance from polling personnel', '07-No guidance from polling personnel'),
                  ('99-Others(please specify)', '99-Others(please specify)')
                  )
    d7_choices = (('01-My name was not on the electoral roll', '01-My name was not on the electoral roll'),
                  ('02-I was not in my consituency', '02-I was not in my consituency'),
                  ('03-I did not have my electoral photo ID card(EPIC)',
                   '03-I did not have my electoral photo ID card(EPIC)'),
                  ('04-I did not know my polling station', '04-I did not know my polling station'),
                  ('05-Polling station was at a distance (logistic problem)',
                   '05-Polling station was at a distance (logistic problem)'),
                  ('06-Long queue and I did not have time', '06-Long queue and I did not have time'),
                  ('07-I felt insecure to go to the polling station',
                   '07-I felt insecure to go to the polling station'),
                  ('08-There was no candidate of my choice/liking', '08-There was no candidate of my choice/liking'),
                  ('09-I just did not want to vote as nothing will change/ No faith in political system',
                   '09-I just did not want to vote as nothing will change/ No faith in political system'),
                  ('10-Voting in national or Assembly elections doesn\'t make a difference, I vote only in \
                  local election', '10-Voting in national or Assembly elections doesn\'t make a difference, I vote \
                  only in local election'),
                  ('11-Polling station was not accessible', '11-Polling station was not accessible'),
                  ('99-Others(please specify)', '99-Others(please specify)')
                  )
    e2_choices = (('0-18th Birthday', '0-18th Birthday'), ('1-1st January', '1-1st January'),
                  ('99-Don’t Know', '99-Don’t Know'))
    e3_choices = (('0-Incorrect Date', '0-Incorrect Date'), ('1-Correct date', '1-Correct date'),
                  ('99-Don\'t know', '99-Don\'t know'))
    e4_choices = (('1-Yes, saw it when I cast my vote', '1-Yes, saw it when I cast my vote'),
                  ('2-Yes, have seen one in electoral literacy programme',
                   '1-Yes, have seen one in electoral literacy programme'),
                  ('3-Yes, have heard/read about it', '3-Yes, have heard/read about it'), ('4-No', '4-No')
                  )
    e5_choices = (('1-Strongly disagree', '1-Strongly disagree'), ('2-Disagree', '2-Disagree'),
                  ('3-Neither agree nor disagree', '3-Neither agree nor disagree'), ('4-Agree', '4-Agree'),
                  ('5-Strongly agree', '5-Strongly agree')
                  )
    f2_choices = (('1-Newspapers/magazines', '1-Newspapers/magazines'), ('2-TV advertisements and programmes',
                                                                         '2-TV advertisements and programmes'),
                  ('3-Radio and FM channels', '3-Radio and FM channels'),
                  ('4-Advertisements in cinemas', '4-Advertisements in cinemas'),
                  ('5-Activity like Rallies, Prabhat Pheris, loudspeaker announcement',
                   '5-Activity like Rallies, Prabhat Pheris, loudspeaker announcement'),
                  ('6-Cultural/entertainments programmes', '6-Cultural/entertainments programmes'),
                  ('7-Government offices circular', '7-Government offices circular'),
                  ('8-Posters, hoardings and publicity materials', '8-Posters, hoardings and publicity materials'),
                  ('9-NGO and Civil society Group', '9-NGO and Civil society Group'),
                  ('10-Internet/ Social Media/Whatsapp', '10-Internet/ Social Media/Whatsapp'), ('11-SMS', '11-SMS'),
                  ('12-Pledge letters/Sankalp patras through school students in the family',
                   '12-Pledge letters/Sankalp patras through school students in the family'),
                  ('13-At Polling Station', '13-At Polling Station'),
                  ('99-Others (please specify)', '99-Others (please specify)')
                  )
    f3_choices = (('01-Date of voting and schedules', '01-Date of voting and schedules'),
                  ('02-Voting is my right and duty', '02-Voting is my right and duty'),
                  ('03-Cast vote as per choice and without taking any inducement',
                   '03-Cast vote as per choice and without taking any inducement'),
                  ('04-#GoRegister or Register', '04-#GoRegister or Register'),
                  ('05-#GoVerify or Verify name in voter list', '05-#GoVerify or Verify name in voter list'),
                  ('06-12 Identity documents allowed for Voting', '06-12 Identity documents allowed for Voting'),
                  ('07-Facilities provided at polling station', '07-Facilities provided at polling station'),
                  ('08-Priority voting for old and PwDs', '08-Priority voting for old and PwDs'),
                  ('09-Voter helpline 1950 or Voter helpline app', '09-Voter helpline 1950 or Voter helpline app'),
                  ('10-cVIGIL app related', '10-cVIGIL app related'), ('11-NVSP portal', '11-NVSP portal'),
                  ('99-Others (please specify)', '99-Others (please specify)')
                  )
    f5_choices = (('1-Ex-President APJ Abdul Kalam', '1-Ex-President APJ Abdul Kalam'),
                  ('2-Cricketer M.S. Dhoni', '2-Cricketer M.S. Dhoni'),
                  ('3-Sportsperson Mary Kom', '3-Sportsperson Mary Kom'),
                  ('4-Sportsperson Saina Nehwal', '4-Sportsperson Saina Nehwal'),
                  ('5-Actor Aamir Khan', '5-Actor Aamir Khan'),
                  ('99-Others (please specify)', '99-Others (please specify)')
                  )
    f7_choices = (('1-To search name and other details on the Electoral Roll',
                   '1-To search name and other details on the Electoral Roll'),
                  ('2-To register/ make modifications online', '2-To register/ make modifications online'),
                  ('3-To download registration forms', '3-To download registration forms'),
                  ('4-To know polling details', '4-To know polling details'),
                  ('5-To know election results', '5-To know election results'),
                  ('6-To know details about the candidates/political parties',
                   '6-To know details about the candidates/political parties'),
                  ('7-To participate in online contests', '7-To participate in online contests'),
                  ('99-Others (please specify)', '99-Others (please specify)')
                  )
    f9_choices = (('0-None of the two', '0-None of the two'), ('1-Voter Helpline no 1950', '1-Voter Helpline no 1950'),
                  ('2-Voter Helpline app only', '2-Voter Helpline app only'), ('3-Both of them', '3-Both of them')
                  )
    f10_choices = (('1-To know about registration or voting process', '1-To know about registration or voting process'),
                   ('2-To verify name on voter list', '2-To verify name on voter list'),
                   ('3-To know my polling station', '3-To know my polling station'),
                   ('4-To know details of my BLO', '4-To know details of my BLO'),
                   ('5-To register a complaint', '5-To register a complaint'),
                   ('99-Others (please specify)', '99-Others (please specify)')
                   )
    g1_choices = (('1-Illiterate', '1-Illiterate'), ('2-Primary school', '2-Primary school'),
                  ('3-High School', '3-High School'), ('4-Higher secondary', '4-Higher secondary'),
                  ('5-Diploma/ Certificate', '5-Diploma/ Certificate'),
                  ('6-Graduate & above including professional/ Technical Courses',
                   '6-Graduate & above including professional/ Technical Courses')
                  )
    g2_choices = (('1-Student', '1-Student'), ('2-Unemployed', '2-Unemployed'),
                  ('3-unemployed available for work', '3-unemployed available for work'),
                  ('4-Government Service', '4-Government Service'), ('5-Private Service', '5-Private Service'),
                  ('6-Own enterprise', '6-Own enterprise'),
                  ('7-Labourer/ Cultivator/ Agricultural and allied activities',
                   '7-Labourer/ Cultivator/ Agricultural and allied activities'), ('8-Home maker', '8-Home maker'),
                  ('99-Others (please specify)', '99-Others (please specify)'),
                  )
    g3_choices = (('1-Never married', '1-Never married'), ('2-Married, no gauna', '2-Married, no gauna'),
                  ('3-Married', '3-Married'), ('4-Widowed', '4-Widowed'),
                  ('5-Separated/divorced', '5-Separated/divorced'))
    g4_choices = (('1-SC', '1-SC'), ('2-ST', '2-ST'), ('3-OBC', '3-OBC'), ('4-Others', '4-Others'))
    g5_choices = (('1-Almost every day', '1-Almost every day'), ('2-At least once a weak', '2-At least once a weak'),
                  ('3-Less than once a weak', '3-Less than once a weak'), ('4-Not for all', '4-Not for all'))
    g6_choices = (('1-Newspapers/magazines', '1-Newspapers/magazines'), ('2-Television', '2-Television'),
                  ('3-Radio', '3-Radio'), ('4-Internet', '4-Internet'), ('5-Mobile Phone', '5-Mobile Phone'),
                  ('6-Family/relatives/friends', '6-Family/relatives/friends'),
                  ('99-Others (please specify)', '99-Others (please specify)')
                  )

    user = models.ForeignKey(to=User, on_delete=models.CASCADE, verbose_name=_('Surveyor'), related_name=_('surveys'))
    a1 = models.CharField(max_length=24, verbose_name=_('a1'), choices=a1_choices)
    a2 = models.TextField(verbose_name=_('a2'))
    a3 = models.TextField(verbose_name=_('a3'), choices=a3_choices)
    a3_code = models.IntegerField(verbose_name=_('a3_code'), choices=a3_code_choices)
    a4 = models.CharField(max_length=8, verbose_name=_('a4'), choices=a4_choices)
    a5 = models.TextField(verbose_name=_('a5'), blank=True, null=True, choices=a5_choices)
    a5_code = models.TextField(verbose_name=_('a5'), blank=True, null=True, choices=a5_code_choices)
    a6 = models.TextField(verbose_name=_('a6'))
    a7 = models.TextField(verbose_name=_('a7'))
    a8 = models.TextField(verbose_name=_('a8'))
    a9 = models.TextField(verbose_name=_('a9'), blank=True, null=True)
    a10 = models.TextField(verbose_name=_('a10'), blank=True, null=True)
    a11 = models.TextField(verbose_name=_('a11'), blank=True, null=True)
    a12 = models.CharField(max_length=64, verbose_name=_('a12'), choices=a12_choices)
    a13 = models.TextField(verbose_name=_('a13'))
    a14 = models.TextField(verbose_name=_('a14'))
    a15 = models.CharField(max_length=16, verbose_name=_('a15'), choices=bool_choices)
    a16 = models.CharField(max_length=16, verbose_name=_('a16'), choices=bool_choices)
    a17 = models.CharField(max_length=16, verbose_name=_('a17'), choices=bool_choices)
    b1 = models.IntegerField(verbose_name=_('b1'), default=1)
    b2 = models.IntegerField(verbose_name=_('b2'), default=0)
    b12 = models.IntegerField(verbose_name=_('b12'), default=0)
    b13 = models.IntegerField(verbose_name=_('b13'), default=0)
    c1 = models.IntegerField(verbose_name=_('c1'), default=98)
    c2 = models.CharField(max_length=128, verbose_name=_('c2'), choices=null_boolean_choices, blank=True, null=True)
    c3 = models.CharField(max_length=128, verbose_name=_('c3'), choices=c3_choices)
    c4 = models.CharField(max_length=128, verbose_name=_('c4'), choices=bool_choices, blank=True, null=True)
    c5 = models.CharField(max_length=128, verbose_name=_('c5'), choices=c5_choices, blank=True, null=True)
    c6 = models.CharField(max_length=128, verbose_name=_('c6'), choices=c6_choices, blank=True, null=True)
    c7 = models.CharField(max_length=128, verbose_name=_('c7'), choices=c7_choices, blank=True, null=True)
    c8 = models.CharField(max_length=128, verbose_name=_('c8'), choices=bool_choices, blank=True, null=True)
    c9 = models.CharField(max_length=128, verbose_name=_('c9'), choices=c9_choices, blank=True, null=True)
    c10 = models.CharField(max_length=128, verbose_name=_('c10'), choices=c10_choices, blank=True, null=True)
    d1 = models.CharField(max_length=128, verbose_name=_('d1'), choices=bool_choices)
    d2 = models.CharField(max_length=128, verbose_name=_('d2'), choices=d2_choices, blank=True, null=True)
    d3a = models.CharField(max_length=128, verbose_name=_('d3a'), choices=null_boolean_choices, blank=True, null=True)
    d3b = models.CharField(max_length=128, verbose_name=_('d3b'), choices=null_boolean_choices, blank=True, null=True)
    d3c = models.CharField(max_length=128, verbose_name=_('d3c'), choices=null_boolean_choices, blank=True, null=True)
    d3d = models.CharField(max_length=128, verbose_name=_('d3d'), choices=null_boolean_choices, blank=True, null=True)
    d3e = models.CharField(max_length=128, verbose_name=_('d3e'), choices=null_boolean_choices, blank=True, null=True)
    d3f = models.CharField(max_length=128, verbose_name=_('d3f'), choices=null_boolean_choices, blank=True, null=True)
    d3g = models.CharField(max_length=128, verbose_name=_('d3g'), choices=null_boolean_choices, blank=True, null=True)
    d3h = models.CharField(max_length=128, verbose_name=_('d3h'), choices=null_boolean_choices, blank=True, null=True)
    d3i = models.CharField(max_length=128, verbose_name=_('d3i'), choices=null_boolean_choices, blank=True, null=True)
    d3j = models.CharField(max_length=128, verbose_name=_('d3j'), choices=null_boolean_choices, blank=True, null=True)
    d3k = models.CharField(max_length=128, verbose_name=_('d3k'), choices=null_boolean_choices, blank=True, null=True)
    d4 = models.CharField(max_length=8, verbose_name=_('d4'), choices=bool_choices, blank=True, null=True)
    d5 = models.CharField(max_length=128, verbose_name=_('d5'), choices=d5_choices, blank=True, null=True)
    d7 = models.CharField(max_length=128, verbose_name=_('d7'), choices=d7_choices, blank=True, null=True)
    e1 = models.IntegerField(verbose_name=_('e1'), default=99, blank=True, null=True)
    e2 = models.CharField(max_length=128, verbose_name=_('e2'), choices=e2_choices)
    e3 = models.CharField(max_length=128, verbose_name=_('e3'), choices=e3_choices)
    e4a = models.CharField(max_length=128, verbose_name=_('e4a'), choices=e4_choices)
    e4b = models.CharField(max_length=128, verbose_name=_('e4b'), choices=e4_choices)
    e4c = models.CharField(max_length=128, verbose_name=_('e4c'), choices=e4_choices)
    e5a = models.CharField(max_length=128, verbose_name=_('e5a'), choices=e5_choices)
    e5b = models.CharField(max_length=128, verbose_name=_('e5b'), choices=e5_choices)
    e5c = models.CharField(max_length=128, verbose_name=_('e5c'), choices=e5_choices)
    e5d = models.CharField(max_length=128, verbose_name=_('e5d'), choices=e5_choices)
    e5e = models.CharField(max_length=128, verbose_name=_('e5e'), choices=e5_choices)
    e5f = models.CharField(max_length=128, verbose_name=_('e5f'), choices=e5_choices)
    e5g = models.CharField(max_length=128, verbose_name=_('e5g'), choices=e5_choices)
    e5h = models.CharField(max_length=128, verbose_name=_('e5h'), choices=e5_choices)
    f1 = models.CharField(max_length=128, verbose_name=_('f1'), choices=null_boolean_choices)
    f2 = models.CharField(max_length=128, verbose_name=_('f2'), choices=f2_choices)
    f3 = models.CharField(max_length=128, verbose_name=_('f3'), choices=f3_choices)
    f4a = models.CharField(max_length=128, verbose_name=_('f4a'), choices=bool_choices, blank=True, null=True)
    f4b = models.CharField(max_length=128, verbose_name=_('f4b'), choices=bool_choices, blank=True, null=True)
    f4c = models.CharField(max_length=128, verbose_name=_('f4c'), choices=bool_choices, blank=True, null=True)
    f5 = models.CharField(max_length=128, verbose_name=_('f5'), choices=f5_choices)
    f6 = models.CharField(max_length=128, verbose_name=_('f6'), choices=null_boolean_choices)
    f7 = models.CharField(max_length=128, verbose_name=_('f7'), choices=f7_choices)
    f8 = models.CharField(max_length=128, verbose_name=_('f8'), choices=somewhat_choices)
    f9 = models.CharField(max_length=128, verbose_name=_('f9'), choices=f9_choices, blank=True, null=True)
    f10 = models.CharField(max_length=128, verbose_name=_('f10'), choices=f10_choices)
    f11 = models.CharField(max_length=128, verbose_name=_('f11'), choices=somewhat_choices)
    g1 = models.CharField(max_length=128, verbose_name=_('g1'), choices=g1_choices, blank=True, null=True)
    g2 = models.CharField(max_length=128, verbose_name=_('g2'), choices=g2_choices)
    g3 = models.CharField(max_length=128, verbose_name=_('g3'), choices=g3_choices)
    g4 = models.CharField(max_length=128, verbose_name=_('g4'), choices=g4_choices)
    g5a = models.CharField(max_length=128, verbose_name=_('g5a'), choices=g5_choices)
    g5b = models.CharField(max_length=128, verbose_name=_('g5b'), choices=g5_choices)
    g5c = models.CharField(max_length=128, verbose_name=_('g5c'), choices=g5_choices)
    g5d = models.CharField(max_length=128, verbose_name=_('g5d'), choices=g5_choices)
    g6 = models.CharField(max_length=128, verbose_name=_('g6'), choices=g6_choices)
    h1 = models.CharField(max_length=128, verbose_name=_('h1'), choices=bool_choices)
    h2 = models.CharField(max_length=128, verbose_name=_('h2'), choices=bool_choices)
    h3 = models.CharField(max_length=128, verbose_name=_('h3'), blank=True, null=True)
    h4 = models.CharField(max_length=128, verbose_name=_('h4'), blank=True, null=True)
    started_at = models.DateTimeField(blank=True, null=True)
    completed_at = models.DateTimeField(blank=True, null=True)
    latitude = models.FloatField(verbose_name=_('Latitude'), blank=True, null=True)
    longitude = models.FloatField(verbose_name=_('Longitude'), blank=True, null=True)

    class Meta:
        db_table = _('survey')
        verbose_name = _('Survey')
        verbose_name_plural = _('Surveys')


class FamilyDetails(models.Model):
    relationship_choices = (('01-Head', '01-Head'), ('02-Wife/Husband', '02-Wife/Husband'), ('03-Son/Daughter',
                                                                                             '03-Son/Daughter'),
                            ('04-Son in law/ daughter in law', '04-Son in law/ daughter in law'),
                            ('05-Grandchild', '05-Grandchild'), ('06-Father/Mother', '06-Father/Mother'),
                            ('07-Brother/Sister', '07-Brother/Sister'), ('08-Father-in-law/Mother-in-law',
                                                                         '08-Father-in-law/Mother-in-law'),
                            ('09-Nephew/Niece', '09-Nephew/Niece'), ('10-Brother-in-law/Sister-in-law',
                                                                     '10-Brother-in-law/Sister-in-law'),
                            ('11-Other relatives', '11-Other relatives'), ('12-Servant/Others', '12-Servant/Others')
                            )
    sex_choices = (('1-Male', '1-Male'), ('2-Female', '2-Female'), ('3-Third Gender', '3-Third Gender'))
    disability_choices = (('0-No', '0-No'), ('1-Yes(in seeing)', '1-Yes(in seeing)'), ('2-Yes(in speech)',
                                                                                       '2-Yes(in speech)'),
                          ('3-Yes(in hearing)', '3-Yes(in hearing)'), ('4-Yes(in movement)', '4-Yes(in movement)')
                          )
    enroll_choices = (('0-No', '0-No'), ('1-Yes(application in progress)', '1-Yes(application in progress)'),
                      ('2-Yes(currently enrolled)', '2-Yes(currently enrolled)')
                      )

    survey = models.ForeignKey(to=Survey, on_delete=models.CASCADE, verbose_name=_('Survey_ID'),
                               related_name=_('family_details'))
    s_no = models.IntegerField(verbose_name=_('S#'), default=1)
    name = models.CharField(max_length=128, verbose_name=_('Name'))
    relationship = models.CharField(max_length=128, verbose_name=_('Relationship with HH'),
                                    choices=relationship_choices)
    sex = models.CharField(max_length=128, verbose_name=_('Sex'), choices=sex_choices)
    disabled = models.CharField(max_length=128, verbose_name=_('Disabled'), choices=disability_choices)
    migration = models.CharField(max_length=128, verbose_name=_('Migrated in last 1 year'), choices=bool_choices)
    enrolled = models.CharField(max_length=128, verbose_name=_('Enrolled'), choices=enroll_choices)
    has_voted_in_lok_sabha = models.CharField(max_length=128, verbose_name=_('Voted in Lok Sabha'),
                                              choices=bool_choices)
    has_voted_in_assembly = models.CharField(max_length=128, verbose_name=_('Voted in Assembly election'),
                                             choices=bool_choices)

    class Meta:
        db_table = _('family_details')
        verbose_name = _('Family Details')
        verbose_name_plural = _('Family Details')
