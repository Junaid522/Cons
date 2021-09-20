# Generated by Django 3.1.2 on 2020-12-25 15:30

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(help_text='City Name', max_length=255, verbose_name=' City Name')),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'ordering': ('-updated_at', '-created_at'),
                'get_latest_by': 'updated_at',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(help_text='Country Name', max_length=255, verbose_name='Country Name')),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'ordering': ('-updated_at', '-created_at'),
                'get_latest_by': 'updated_at',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(help_text='Course Name', max_length=255)),
                ('course_description', models.TextField(blank=True, null=True)),
                ('course_language', models.CharField(max_length=100)),
                ('total_credit_hours', models.CharField(blank=True, max_length=100, null=True)),
                ('dual_medium', models.CharField(blank=True, max_length=100, null=True)),
                ('course_entry_requirements', models.TextField(blank=True, null=True)),
                ('progression_degrees', models.TextField(blank=True, null=True)),
                ('progression_universities', models.TextField(blank=True, null=True)),
                ('course_scholarship_details', models.TextField(blank=True, null=True)),
                ('recommendation_letters', models.IntegerField(blank=True, null=True)),
                ('entry', models.CharField(blank=True, choices=[('pathway', 'Pathway'), ('direct', 'Direct')], max_length=25, null=True)),
                ('ielts_waiver_test', models.TextField(blank=True, null=True)),
                ('apply_portal', models.CharField(blank=True, choices=[('uni_assist', 'Uni Assist'), ('direct', 'Direct')], max_length=25, null=True)),
            ],
            options={
                'ordering': ('-updated_at', '-created_at'),
                'get_latest_by': 'updated_at',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CourseTitle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('key', models.CharField(max_length=100, unique=True)),
                ('display_name', models.CharField(help_text='Associate degree Title ie BA,Bsc,Bs', max_length=255, unique=True)),
            ],
            options={
                'ordering': ('-updated_at', '-created_at'),
                'get_latest_by': 'updated_at',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('key', models.CharField(max_length=100, unique=True)),
                ('display_name', models.CharField(help_text='Currency must be unique', max_length=255, unique=True)),
            ],
            options={
                'ordering': ('-updated_at', '-created_at'),
                'get_latest_by': 'updated_at',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DegreeLevel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('key', models.CharField(max_length=100, unique=True)),
                ('display_name', models.CharField(help_text='DegreeLevel ie Bachelor,Master ', max_length=255, unique=True, verbose_name='DegreeLevel')),
            ],
            options={
                'ordering': ('-updated_at', '-created_at'),
                'get_latest_by': 'updated_at',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Discipline',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('key', models.CharField(max_length=100, unique=True)),
                ('name', models.CharField(help_text='Discipline', max_length=255, unique=True, verbose_name='Discipline Name')),
                ('description', models.TextField()),
            ],
            options={
                'ordering': ('-updated_at', '-created_at'),
                'get_latest_by': 'updated_at',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Institute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('institute_name', models.CharField(help_text='Institute Name', max_length=255, verbose_name='Institute Name')),
                ('institute_type', models.CharField(choices=[('COLLEGE', 'College'), ('UNIVERSITY', 'University'), ('TAFE', 'TAFE College'), ('PATHWAY_COLLEGE', 'Pathway College'), ('PATHWAY_UNIVERSITY', 'Pathway University')], default='UNIVERSITY', help_text='Institute Type ie college or university', max_length=25)),
                ('sector', models.CharField(choices=[('PUBLIC', 'Public'), ('PRIVATE', 'Private')], default='PRIVATE', help_text='Institute sector ie public or private', max_length=25)),
                ('institute_panel', models.CharField(choices=[('p1', 'P1'), ('p2', 'P2'), ('p3', 'P3')], default='p3', help_text='Institute sector ie public or private', max_length=25)),
                ('established', models.CharField(blank=True, help_text='Campus establish establish in which year', max_length=255, null=True)),
                ('institute_description', models.TextField(blank=True, null=True)),
                ('institute_financial_aid_per_year', models.CharField(blank=True, max_length=255, null=True)),
                ('institute_scholarship_amount_per_year', models.CharField(blank=True, max_length=255, null=True)),
                ('institute_scholarship_separate_application_required', models.CharField(choices=[('tbc', 'TBC'), ('yes', 'Yes'), ('no', 'No')], default='tbc', max_length=25)),
                ('institute_scholarship_criteria', models.TextField(blank=True, null=True)),
                ('accommodation_availability', models.CharField(choices=[('tbc', 'TBC'), ('yes', 'Yes'), ('no', 'No')], default='tbc', max_length=25)),
                ('commonapp_university', models.CharField(choices=[('tbc', 'TBC'), ('yes', 'Yes'), ('no', 'No')], default='tbc', max_length=25)),
                ('essay_requirement', models.CharField(choices=[('tbc', 'TBC'), ('yes', 'Yes'), ('no', 'No')], default='tbc', max_length=25)),
            ],
            options={
                'ordering': ('-updated_at', '-created_at'),
                'get_latest_by': 'updated_at',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='InstituteGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('key', models.CharField(help_text='Group short Name key', max_length=255, unique=True)),
                ('display_name', models.CharField(help_text='Group Name', max_length=255)),
                ('content', models.TextField(help_text=' Group content')),
            ],
            options={
                'ordering': ('-updated_at', '-created_at'),
                'get_latest_by': 'updated_at',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PathwayGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('key', models.CharField(help_text='Group short Name key', max_length=255, unique=True)),
                ('display_name', models.CharField(help_text='Group Name', max_length=255)),
                ('description', models.TextField(help_text=' Group content')),
            ],
            options={
                'ordering': ('-updated_at', '-created_at'),
                'get_latest_by': 'updated_at',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Scholarship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('scholarship_name', models.CharField(help_text='Scholarship name', max_length=255)),
                ('scholarship_content', models.TextField(blank=True, null=True)),
                ('scholarship_value', models.TextField()),
                ('nationality', models.TextField()),
                ('scholarship_eligibility', models.TextField(blank=True, null=True)),
                ('how_to_apply', models.TextField(blank=True, null=True)),
                ('scholarship_link', models.URLField(blank=True, max_length=700, null=True)),
                ('scholarship_courses', models.TextField()),
                ('degree_level', models.ManyToManyField(to='constructor.DegreeLevel')),
                ('discipline', models.ManyToManyField(to='constructor.Discipline')),
                ('institute', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='constructor.institute')),
            ],
            options={
                'ordering': ('-updated_at', '-created_at'),
                'get_latest_by': 'updated_at',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ScholarshipType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('key', models.CharField(help_text='Scholarship Type short Name key', max_length=255, unique=True)),
                ('display_name', models.CharField(help_text='Scholarship Type display Name', max_length=255)),
            ],
            options={
                'ordering': ('-updated_at', '-created_at'),
                'get_latest_by': 'updated_at',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Specialization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(help_text='Specialization Name', max_length=255, verbose_name='Specialization')),
            ],
            options={
                'ordering': ('-updated_at', '-created_at'),
                'get_latest_by': 'updated_at',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SubDiscipline',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('key', models.CharField(max_length=100, unique=True)),
                ('name', models.CharField(help_text='Discipline Name', max_length=255, unique=True)),
                ('description', models.TextField()),
                ('discipline', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='constructor.discipline')),
            ],
            options={
                'ordering': ('-updated_at', '-created_at'),
                'get_latest_by': 'updated_at',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(help_text='State Name', max_length=255, verbose_name='State Name')),
                ('region', models.CharField(blank=True, help_text='State Name', max_length=255, null=True)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='constructor.country')),
            ],
            options={
                'ordering': ('-updated_at', '-created_at'),
                'get_latest_by': 'updated_at',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ScholarshipStartDate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('month', models.CharField(choices=[('January', 'January'), ('February', 'February'), ('March', 'March'), ('April', 'April'), ('May', 'May'), ('June', 'June'), ('July', 'July'), ('August', 'August'), ('September', 'September'), ('October', 'October'), ('November', 'November'), ('December', 'December')], max_length=25)),
                ('day', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(31), django.core.validators.MinValueValidator(1)])),
                ('year', models.IntegerField(blank=True, null=True)),
                ('scholarship', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='constructor.scholarship')),
            ],
            options={
                'ordering': ('-updated_at', '-created_at'),
                'get_latest_by': 'updated_at',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ScholarshipCloseDate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('month', models.CharField(choices=[('January', 'January'), ('February', 'February'), ('March', 'March'), ('April', 'April'), ('May', 'May'), ('June', 'June'), ('July', 'July'), ('August', 'August'), ('September', 'September'), ('October', 'October'), ('November', 'November'), ('December', 'December')], max_length=25)),
                ('day', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(31), django.core.validators.MinValueValidator(1)])),
                ('year', models.IntegerField(blank=True, null=True)),
                ('scholarship', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='constructor.scholarship')),
            ],
            options={
                'ordering': ('-updated_at', '-created_at'),
                'get_latest_by': 'updated_at',
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='scholarship',
            name='scholarship_type',
            field=models.ManyToManyField(to='constructor.ScholarshipType'),
        ),
        migrations.CreateModel(
            name='InstituteRanking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('ranking_type', models.CharField(choices=[('qs_world_ranking', ' QS World University Rankings'), ('times_higher_world_ranking', 'Times Higher Education World University Rankings'), ('us_news_world_ranking', 'US News Global Universities Rankings'), ('shanghai_ranking', 'Shanghai Rankings'), ('us_news_national_ranking', 'Shanghai Rankings')], max_length=100)),
                ('value', models.CharField(max_length=255)),
                ('institute', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='constructor.institute')),
            ],
            options={
                'ordering': ('-updated_at', '-created_at'),
                'get_latest_by': 'updated_at',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='InstituteCampus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('campus', models.CharField(help_text='Institute Campus Name', max_length=255)),
                ('address', models.TextField(help_text='Full addresss')),
                ('latitude', models.FloatField(help_text='latitude')),
                ('longitude', models.FloatField(help_text='longitude')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='constructor.city')),
                ('institute', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='constructor.institute')),
            ],
            options={
                'ordering': ('-updated_at', '-created_at'),
                'get_latest_by': 'updated_at',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='InstituteAcceptingRatio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('accepting_type', models.CharField(choices=[('institute_acceptance_ratio_bachelor', ' Bachelor'), ('institute_acceptance_ratio_master', 'Master')], max_length=100)),
                ('value', models.CharField(max_length=255)),
                ('institute', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='constructor.institute')),
            ],
            options={
                'ordering': ('-updated_at', '-created_at'),
                'get_latest_by': 'updated_at',
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='institute',
            name='institute_group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='constructor.institutegroup'),
        ),
        migrations.AddField(
            model_name='institute',
            name='pathway_group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='constructor.pathwaygroup'),
        ),
        migrations.CreateModel(
            name='CourseIntakeAndDeadLine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('intake_month', models.CharField(blank=True, choices=[('January', 'January'), ('February', 'February'), ('March', 'March'), ('April', 'April'), ('May', 'May'), ('June', 'June'), ('July', 'July'), ('August', 'August'), ('September', 'September'), ('October', 'October'), ('November', 'November'), ('December', 'December')], max_length=25, null=True)),
                ('intake_day', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(31), django.core.validators.MinValueValidator(1)])),
                ('intake_year', models.IntegerField(blank=True, null=True)),
                ('deadline_day', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(31), django.core.validators.MinValueValidator(1)])),
                ('deadline_months', models.CharField(blank=True, choices=[('January', 'January'), ('February', 'February'), ('March', 'March'), ('April', 'April'), ('May', 'May'), ('June', 'June'), ('July', 'July'), ('August', 'August'), ('September', 'September'), ('October', 'October'), ('November', 'November'), ('December', 'December')], max_length=25, null=True)),
                ('deadline_year', models.IntegerField(blank=True, null=True)),
                ('application_open_day', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(31), django.core.validators.MinValueValidator(1)])),
                ('application_open_months', models.CharField(blank=True, choices=[('January', 'January'), ('February', 'February'), ('March', 'March'), ('April', 'April'), ('May', 'May'), ('June', 'June'), ('July', 'July'), ('August', 'August'), ('September', 'September'), ('October', 'October'), ('November', 'November'), ('December', 'December')], max_length=25, null=True)),
                ('application_open_year', models.IntegerField(blank=True, null=True)),
                ('rolling_intake', models.BooleanField(default=False, help_text='student can start studying any month ')),
                ('rolling_deadline', models.BooleanField(default=False, help_text='student can apply for admission any time')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='constructor.course')),
            ],
            options={
                'ordering': ('-updated_at', '-created_at'),
                'get_latest_by': 'updated_at',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CourseFee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('type', models.CharField(choices=[('fee_per_year', 'Per Year Fee'), ('application_fee', 'Application Fee'), ('no_application_fee', 'Application Fee not Required'), ('total_pathway_fee', 'Total Pathway Fee'), ('direct_entry_fee_per_semester', 'Direct Entry Fee Per Semester')], max_length=100)),
                ('ceil_value', models.FloatField(blank=True, null=True)),
                ('floor_value', models.FloatField(blank=True, null=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='constructor.course')),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='constructor.currency')),
            ],
            options={
                'ordering': ('-updated_at', '-created_at'),
                'get_latest_by': 'updated_at',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CourseExam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('exam_type', models.CharField(choices=[('sat1', 'sat1'), ('sat2', 'sat2'), ('act', 'act'), ('gre', 'gre'), ('gmat', 'gmat'), ('ielts', 'ielts'), ('gpa', 'gpa')], max_length=25)),
                ('required', models.BooleanField(default=False)),
                ('score', models.FloatField(blank=True, null=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='constructor.course')),
            ],
            options={
                'ordering': ('-updated_at', '-created_at'),
                'get_latest_by': 'updated_at',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CourseDuration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('type', models.CharField(choices=[('year', 'Year'), ('semester', 'Semester')], max_length=25)),
                ('duration_one', models.FloatField()),
                ('duration_two', models.FloatField(blank=True, null=True)),
                ('duration_three', models.FloatField(blank=True, null=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='constructor.course')),
            ],
            options={
                'ordering': ('-updated_at', '-created_at'),
                'get_latest_by': 'updated_at',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CourseApply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('type', models.CharField(blank=True, choices=[('course_detail_web_link', 'Course detail Web Link'), ('course_fee_web_link', 'Course Fee Web Link'), ('course_apply_web_link', 'Course Apply Web Link')], max_length=25, null=True)),
                ('url', models.URLField(blank=True, max_length=1000, null=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='constructor.course')),
            ],
            options={
                'ordering': ('-updated_at', '-created_at'),
                'get_latest_by': 'updated_at',
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='course',
            name='campus',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='constructor.institutecampus'),
        ),
        migrations.AddField(
            model_name='course',
            name='course_title',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='constructor.coursetitle'),
        ),
        migrations.AddField(
            model_name='course',
            name='degree_level',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='constructor.degreelevel'),
        ),
        migrations.AddField(
            model_name='course',
            name='discipline',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='constructor.discipline'),
        ),
        migrations.AddField(
            model_name='course',
            name='specialization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='constructor.specialization'),
        ),
        migrations.AddField(
            model_name='city',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='constructor.state'),
        ),
    ]