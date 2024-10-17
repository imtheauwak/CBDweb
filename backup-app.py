from flask import Flask, render_template, request, redirect, url_for, session
from forms import *
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, RadioField, BooleanField
from wtforms.validators import DataRequired
from flask import flash

output_dict = {f'id_{i}': 0 for i in range(371)}

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mykey'


@app.route('/')
def welcome():
    return render_template('welcome.html')

@app.route('/info', methods=['GET', 'POST'])
def info():
    form = InfoForm()
    if form.validate_on_submit():
        fullname = form.fullname.data
        age = form.age.data
        gender = form.gender.data
        pregnant = form.pregnant.data

        session['output_data'] = {"name": fullname, "age": age, "gender": gender, "pregnant": pregnant}
        # process_output_data(session['output_data'])

        if gender == 'female' and pregnant:
            return redirect(url_for('pregnant_page'))
        else:
            return redirect(url_for('respiratory_page'))
        
    return render_template('info.html', form=form)

@app.route('/pregnant',  methods=['GET', 'POST'])
def pregnant_page():
    form = PregnantForm()
    if form.validate_on_submit():
        # print("Form submitted and validated")
        preg_time = form.preg_time.data
        preg_ = form.preg_.data
        uterus_time = form.uterus_time.data
        preg_status = form.preg_status.data

        if preg_time >= 20:
            output_dict['id_119'] = 1
            output_dict['id_129'] = 1
        elif preg_time < 20:
            output_dict['id_288'] = 1
        else:
            print('error')

        if preg_ == '1st_preg':
            if uterus_time >= 2:
                output_dict['id_290'] = 1
            elif uterus_time < 2:
                output_dict['id_121'] = 1
            else:
                print('error')
        else:
            if uterus_time >= 5:
                output_dict['id_289'] = 1
            elif uterus_time < 5:
                output_dict['id_122'] = 1
            else:
                print('error')

        if preg_status == 'id_318':
            output_dict['id_318'] = 1
        elif preg_status == 'id_120':
            output_dict['id_120'] = 1
        elif preg_status == 'id_124':
            output_dict['id_124'] = 1
        elif preg_status == 'id_125':
            output_dict['id_125'] = 1
        elif preg_status == 'id_123':
            output_dict['id_123'] = 1
        else:
            pass

        
        
            

        return redirect(url_for('respiratory_page'))
        
    return render_template("pregnant.html", form=form)

@app.route('/respiratory', methods=['GET', 'POST'])
def respiratory_page():
    form = RespiratoryForm()
    if form.validate_on_submit():

        if form.breath.data == 'canbreath':
            if form.breathable.data == 'loud':
                if form.id_15.data:
                    output_dict['id_15'] = 1
            elif form.breathable.data == 'swift':
                if form.id_16.data:
                    output_dict['id_16'] = 1
                if form.id_20.data:
                    output_dict['id_20'] = 1 
                if form.id_5.data:
                    output_dict['id_5'] = 1
            if session['age'] > 25:
                if form.breathable.data == 'stuck':
                    if form.id_6.data:
                        output_dict['id_6'] = 1

                    if form.id_7.data:
                        output_dict['id_7'] = 1

                    if form.id_8.data:
                        output_dict['id_8'] = 1

                    if form.id_12.data:
                        output_dict['id_12'] = 1

                    if form.id_9.data:
                        output_dict['id_9'] = 1

                    if form.id_14.data:
                        output_dict['id_14'] = 1

                    if form.id_22.data:
                        output_dict['id_22'] = 1

                    if form.id_23.data:
                        output_dict['id_23'] = 1
            else:
                pass

        elif form.breath.data == 'cannotbreath':
            output_dict['id_0'] = 1

        elif form.breath.data == 'id_11':
            output_dict['id_11'] = 1

        
        if form.id_13.data:
            output_dict['id_13'] = 1

        
        if form.to_breath.data == 'id_1':
            output_dict['id_1'] = 1
        elif form.to_breath.data == 'id_2':
            output_dict['id_2'] = 1
        elif form.to_breath.data == 'id_3':
            output_dict['id_3'] = 1

     
        # Redirect to the next page
        return redirect(url_for('conciousness_page'))
    else:
        print("Form did not validate:", form.errors)

    return render_template("respiratory.html", form=form)


@app.route('/conciousness', methods=['GET', 'POST'])
def conciousness_page():
    form = ConciousnessForm()
    if form.validate_on_submit():
        
        if form.conciousness.data == 'concious':
            if form.id_331.data:
                output_dict['id_331'] = 1

            if form.id_337.data:
                output_dict['id_337'] = 1

            if form.id_327.data:
                output_dict['id_327'] = 1

            if form.id_307.data:
                output_dict['id_307'] = 1

            if form.id_308.data:
                output_dict['id_308'] = 1

            # Check the 'hangover' RadioField
            if form.hangover.data == 'alcohol':
                output_dict['alcohol'] = 1
            elif form.hangover.data == 'id_314':
                output_dict['id_314'] = 1
            elif form.hangover.data == 'both':
                output_dict['both'] = 1

            # Check the 'alcohol_' RadioField
            if form.alcohol_.data == 'id_313':
                output_dict['id_313'] = 1
            elif form.alcohol_.data == 'id_312':
                output_dict['id_312'] = 1
            elif form.alcohol_.data == 'alc_309':
                if session['age'] < 17:
                    output_dict['alc_309'] = 1

            # Check the 'alc_drg' RadioField
            if form.alc_drg.data == 'id_311':
                output_dict['id_311'] = 1
            elif form.alc_drg.data == 'id_310':
                output_dict['id_310'] = 1
            elif form.alc_drg.data == 'id_333':
                output_dict['id_333'] = 1
            elif form.conciousness.data == 'id_297':
                output_dict['id_297'] = 1
        else:
            pass
        # Check the 'id_335' BooleanField
        if form.id_335.data:
            output_dict['id_335'] = 1

        # Check the 'id_336' RadioField
        if form.id_336.data == 'canwake':
            output_dict['id_336'] = 1
        else:
            pass

        # Check the 'noconcioussub' RadioField
        if form.noconcioussub.data == 'id_329':
            output_dict['id_329'] = 1
        elif form.noconcioussub.data == 'id_330':
            output_dict['id_330'] = 1
        elif form.noconcioussub.data == 'id_333':
            output_dict['id_333'] = 1

       
        

        # Check for pain-related BooleanFields
        if form.id_289.data:
            output_dict['id_289'] = 1

        if form.headache.data:
            if form.id_305.data:
                output_dict['id_305'] = 1

            if form.id_306.data:
                output_dict['id_306'] = 1

            if form.id_328.data:
                output_dict['id_328'] = 1

            if form.id_319.data:
                output_dict['id_319'] = 1

        if form.backache.data:
            if session['age'] > 65:
                 output_dict['id_251'] = 1
            elif session['age'] >= 50:
                 output_dict['id_257'] = 1
            else:
                output_dict['id_265'] = 1

        if form.id_317.data:
            output_dict['id_317'] = 1

        
        if form.lo_tummy.data:
            if session['age'] > 65:
                 output_dict['id_249'] = 1
            elif session['age'] >= 50:
                 output_dict['id_255'] = 1
            else:
                pass


        if form.stomachache.data:
            if session['age'] > 65:
                 output_dict['id_250'] = 1
            elif session['age'] >= 50:
                 output_dict['id_256'] = 1
            else:
                output_dict['id_264'] = 1
            
        if form.stomachhurt.data == 'id_253':
            output_dict['id_253'] = 1
        elif form.stomachhurt.data == 'id_254':
            output_dict['id_254'] = 1
        elif form.stomachhurt.data == 'none':
            pass

        

        # Check for chest-related conditions
        if form.chestache.data:
            if form.id_229.data:
                output_dict['id_229'] = 1

            if form.chestpain.data:
                if session['gender'] == 'male':
                    if session['age'] >= 40:
                        output_dict['id_346'] = 1
                    else:
                        pass
                elif session['gender'] == 'female':
                    if session['age'] >= 45:
                        output_dict['id_347'] = 1
                    else:
                        pass


            if form.chestheart.data:
                if session['gender'] == 'male':
                    if session['age'] >= 40:
                        output_dict['id_283'] = 1
                    else:
                        output_dict['id_286'] = 1
                elif session['gender'] == 'female':
                    if session['age'] >= 45:
                        output_dict['id_284'] = 1
                    else:
                        output_dict['id_287'] = 1

            if form.chestinjury.data:
                if session['gender'] == 'male':
                    if session['age'] >= 40:
                        output_dict['id_295'] = 1
                    else:
                        pass
                elif session['gender'] == 'female':
                    if session['age'] >= 45:
                        output_dict['id_296'] = 1
                    else:
                        pass
            if form.heartchest.data:
                if session['age'] > 40:
                    output_dict['Id_334'] = 1

        if form.id_303.data:
            output_dict['id_303'] = 1

        if form.id_304.data:
            output_dict['id_304'] = 1

        if form.id_320.data:
            output_dict['id_320'] = 1

        if form.id_316.data:
            output_dict['id_316'] = 1

        if form.id_344.data:
            output_dict['id_344'] = 1

        if form.id_322.data:
            output_dict['id_322'] = 1

        

        # Check vision-related RadioField
        if form.vision.data == 'id_301':
            output_dict['id_301'] = 1
        elif form.vision.data == 'id_300':
            output_dict['id_300'] = 1
        elif form.vision.data == 'normal_vision':
            pass

        # Check fever-related RadioField
        if form.fever.data == 'havefever':
            if form.id_325.data:
                output_dict['id_325'] = 1

            if form.id_345.data:
                output_dict['id_345'] = 1

            if form.id_339.data:
                output_dict['id_339'] = 1

            if form.id_342.data:
                if session['age'] < 18:
                    output_dict['id_342'] = 1

        elif form.fever.data == 'nofever':
            pass

        # Check other specific conditions
        if form.id_26.data:
            output_dict['id_26'] = 1

        if form.id_25.data:
            output_dict['id_25'] = 1

        if form.id_321.data:
            output_dict['id_321'] = 1

        
       

        return redirect(url_for('conversation_page'))

    return render_template("conciousness.html", form=form)

@app.route('/conversation', methods=['GET', 'POST'])
def conversation_page():
    form = ConversationForm()
    if form.validate_on_submit():
        
        
        # Assuming you have a form instance called `form`:
        talk = form.talk.data

        # No
        id_35 = form.id_35.data

        # Yes
        id_30 = form.id_30.data

        ## cantalk
        id_32 = form.id_32.data

        ## voice
        id_31 = form.id_31.data
        id_36 = form.id_36.data

        ## hardtotalk (id_39)
        id_38 = form.id_38.data
        id_37 = form.id_37.data
        timeoftalk = form.timeoftalk.data
        id_34 = form.id_34.data

        if talk == 'id_28':
            output_dict['id_28'] = 1
        elif talk == 'id_27':
            output_dict['id_27'] = 1

        # Handling BooleanFields in ConversationForm
        if id_35:
            output_dict['id_35'] = 1
        if id_30:
            output_dict['id_30'] = 1
        if id_32:
            output_dict['id_32'] = 1
        if id_31:
            output_dict['id_31'] = 1
        if id_36:
            output_dict['id_36'] = 1
        if id_38:
            output_dict['id_38'] = 1
        if timeoftalk > 3:
            output_dict['id_37'] = 1
            output_dict['id_40'] = 1
        if id_34:
            output_dict['id_34'] = 1
            if session['age'] and timeoftalk < 3:
                output_dict['id_41'] = 1

   
        return redirect(url_for('movement_page'))
    return render_template("conversation.html", form=form)

@app.route('/movement', methods=['GET', 'POST'])
def movement_page():
    form = MovementForm()
    if form.validate_on_submit():

        # Assuming you have a form instance called `form`:
        id_42 = form.id_42.data
        id_43 = form.id_43.data
        id_44 = form.id_44.data
        id_45 = form.id_45.data
        id_46 = form.id_46.data
        id_47 = form.id_47.data
        id_49 = form.id_49.data
        id_50 = form.id_50.data
        id_51 = form.id_51.data
        id_52 = form.id_52.data
        id_53 = form.id_53.data

        paralyze = form.paralyze.data
        timeparalyzed = form.timeparalyzed.data

        if id_42:
            output_dict['id_42'] = 1
        if id_43:
            output_dict['id_43'] = 1
        if id_44:
            output_dict['id_44'] = 1
        if id_45:
            output_dict['id_45'] = 1
        if id_46:
            output_dict['id_46'] = 1
        if id_47:
            output_dict['id_47'] = 1
        if id_49:
            output_dict['id_49'] = 1
        if id_50:
            output_dict['id_50'] = 1
        if id_51:
            output_dict['id_51'] = 1
        if id_52:
            output_dict['id_52'] = 1
        if id_53:
            output_dict['id_53'] = 1

        # Handling RadioField for paralysis
        if paralyze == 'paralazed':
            if session['age'] > 45:
                if timeparalyzed >= 3:
                    output_dict['id_54'] = 1
                else:
                    output_dict['id_48'] = 1


        elif paralyze == 'notparalyzed':
            pass
        

   
        return redirect(url_for('appearance_page'))
    return render_template("movement.html", form=form)

@app.route('/appearance', methods=['GET', 'POST'])
def appearance_page():
    form = AppearanceForm()
    if form.validate_on_submit():

        if form.conciousness.data == 'concious':
            output_dict['concious'] = 1
        elif form.conciousness.data == 'id_297':
            output_dict['id_297'] = 1

        if form.id_335.data:
            output_dict['id_335'] = 1

        if form.id_336.data == 'canwake':
            output_dict['canwake'] = 1
        elif form.id_336.data == 'cannotwake':
            output_dict['cannotwake'] = 1

        if form.noconcioussub.data == 'id_329':
            output_dict['id_329'] = 1
        elif form.noconcioussub.data == 'id_330':
            output_dict['id_330'] = 1

        # Check for other symptoms
        if form.id_331.data:
            output_dict['id_331'] = 1

        if form.id_337.data:
            output_dict['id_337'] = 1

        if form.id_327.data:
            output_dict['id_327'] = 1

        if form.id_307.data:
            output_dict['id_307'] = 1

        if form.id_308.data:
            output_dict['id_308'] = 1

        # Check for alcohol-related conditions
        if form.hangover.data == 'alcohol':
            output_dict['alcohol'] = 1
        elif form.hangover.data == 'id_314':
            output_dict['id_314'] = 1
        elif form.hangover.data == 'both':
            output_dict['both'] = 1

        if form.alcohol_.data == 'id_313':
            output_dict['id_313'] = 1
        elif form.alcohol_.data == 'id_312':
            output_dict['id_312'] = 1
        elif form.alcohol_.data == 'alc_309':
            output_dict['alc_309'] = 1

        if form.alc_drg.data == 'id_311':
            output_dict['id_311'] = 1
        elif form.alc_drg.data == 'id_310':
            output_dict['id_310'] = 1
        elif form.alc_drg.data == 'id_333':
            output_dict['id_333'] = 1

        # Check for pain-related symptoms
        if form.id_289.data:
            output_dict['id_289'] = 1

        if form.headache.data:
            output_dict['headache'] = 1

        if form.backache.data:
            output_dict['backache'] = 1

        if form.id_317.data:
            output_dict['id_317'] = 1

        if form.lo_tummy.data:
            output_dict['lo_tummy'] = 1

        if form.stomachache.data:
            output_dict['stomachache'] = 1

        if form.stomachhurt.data == 'id_253':
            output_dict['id_253'] = 1
        elif form.stomachhurt.data == 'id_254':
            output_dict['id_254'] = 1
        elif form.stomachhurt.data == 'none':
            output_dict['none'] = 1

        if form.id_305.data:
            output_dict['id_305'] = 1

        if form.id_306.data:
            output_dict['id_306'] = 1

        if form.id_328.data:
            output_dict['id_328'] = 1

        if form.id_319.data:
            output_dict['id_319'] = 1

        # Check for chest-related conditions
        if form.chestache.data:
            output_dict['chestache'] = 1

        if form.id_303.data:
            output_dict['id_303'] = 1

        if form.id_304.data:
            output_dict['id_304'] = 1

        if form.id_320.data:
            output_dict['id_320'] = 1

        if form.id_316.data:
            output_dict['id_316'] = 1

        if form.id_344.data:
            output_dict['id_344'] = 1

        if form.id_322.data:
            output_dict['id_322'] = 1

        if form.id_229.data:
            output_dict['id_229'] = 1

        if form.chestpain.data:
            output_dict['chestpain'] = 1

        if form.chestheart.data:
            output_dict['chestheart'] = 1

        if form.chestinjury.data:
            output_dict['chestinjury'] = 1

        if form.heartchest.data:
            output_dict['heartchest'] = 1

        # Check vision-related conditions
        if form.vision.data == 'id_301':
            output_dict['id_301'] = 1
        elif form.vision.data == 'id_300':
            output_dict['id_300'] = 1
        elif form.vision.data == 'normal_vision':
            output_dict['normal_vision'] = 1

        # Check fever-related conditions
        if form.fever.data == 'havefever':
            output_dict['havefever'] = 1
        elif form.fever.data == 'nofever':
            output_dict['nofever'] = 1

        # Check for other specific conditions
        if form.id_26.data:
            output_dict['id_26'] = 1

        if form.id_25.data:
            output_dict['id_25'] = 1

        if form.id_321.data:
            output_dict['id_321'] = 1

        if form.id_325.data:
            output_dict['id_325'] = 1

        if form.id_345.data:
            output_dict['id_345'] = 1

        if form.id_339.data:
            output_dict['id_339'] = 1

        if form.id_342.data:
            output_dict['id_342'] = 1
   
        return redirect(url_for('condisease_page'))
    return render_template("appearance.html", form=form)

@app.route('/condisease', methods=['GET', 'POST'])
def condisease_page():
    form = ConversationForm()
    if form.validate_on_submit():
        # Assuming you have a form instance called `form`:
        id_349 = form.id_349.data
        id_350 = form.id_350.data
        id_351 = form.id_351.data
        id_352 = form.id_352.data
        id_353 = form.id_353.data
        id_354 = form.id_354.data
        id_355 = form.id_355.data
        id_356 = form.id_356.data




   
        return redirect(url_for('other_page'))
    return render_template("condisease.html", form=form)

@app.route('/other', methods=['GET', 'POST'])
def other_page():
    form = ConversationForm()
    if form.validate_on_submit():
        # Assuming you have a form instance called `form`:
        id_33 = form.id_33.data
        id_357 = form.id_357.data
        id_358 = form.id_358.data
        id_359 = form.id_359.data
        id_360 = form.id_360.data
        id_361 = form.id_361.data
        id_362 = form.id_362.data
        id_363 = form.id_363.data
        id_364 = form.id_364.data
        id_365 = form.id_365.data
        id_366 = form.id_366.data
        id_367 = form.id_367.data
        id_368 = form.id_368.data
        id_369 = form.id_369.data
        id_370 = form.id_370.data



   
        return redirect(url_for('other_page'))
    return render_template("other.html", form=form)

@app.route('/output', methods=['GET', 'POST'])
def output_page():
    
        

   
        
    return render_template("output.html")


def process_output_data(data):
    print(data)

if __name__ == '__main__':
    app.run(debug=True)
