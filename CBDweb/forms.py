from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, RadioField, BooleanField
from wtforms.validators import DataRequired


class InfoForm(FlaskForm):
    fullname = StringField('Fullname', validators=[DataRequired()])
    age = IntegerField('Age', validators=[DataRequired()])
    gender = RadioField('Biological Gender', choices=[('male', 'Male'), ('female', 'Female')], validators=[DataRequired()])
    pregnant = BooleanField('Pregnant')

class PregnantForm(FlaskForm):
    preg_time = IntegerField('อายุครรภ์ (สัปดาห์)', validators=[DataRequired()])
    preg_ = RadioField('ครรภ์แรกหรือไม่', choices=[('1st_preg', 'ใช่'), ('n1st_preg', 'ไม่ใช่')], validators=[DataRequired()])
    uterus_time = IntegerField('การบีบตัวของมดลูก (นาที)', validators=[DataRequired()])
    preg_status = RadioField('มีอาการเหล่านี้หรือไม่', 
                             choices=[('id_318', 'เจ็บท้องคลอด'), ('id_120', 'ทารกกำลังคลอดออกมาโผล่ออกมา'), 
                                      ('id_124', 'ภาวะแทรกซ้อน:สรีระทารก'), ('id_125', 'ถุงน้ำคร่ำแตก(น้ำเดิน)'), 
                                      ('id_123', 'คลอดครั้งก่อนเวลาเจ็บครรภ์<1ชม.')])

class RespiratoryForm(FlaskForm):
    breath = RadioField('หายใจได้หรือไม่', choices=[('canbreath', 'YES'), ('cannotbreath', 'NO'), ('id_11','ทำให้ทางหายใจโล่งได้แล้ว')], validators=[DataRequired()])
    id_13 = BooleanField('ไม่หายใจหลังหยุดชัก')
    to_breath = RadioField('สามารถทำให้หายใจโดย', choices=[('id_1', 'ต้องลุกนั่งเพื่อให้หายใจได้'), ('id_2', 'ต้องพิงผนังเพื่อให้หายใจได้'), ('id_3', 'ต้องยืนเพื่อให้หายใจได้')])
    
    # YES
    breathable = RadioField('ลักษณะการหายใจ', 
                            choices=[('loud', 'เสียงดัง'), ('swift', 'หายใจเร็ว'), ('stuck', 'หายใจขัด'), ('id_18', 'เจ็บขณะหายใจ'),('id_19','ออกซิเจนหมดถัง')], validators=[DataRequired()])
    ## Loud
    id_15 = BooleanField('หายใจดังโครกคราก')

    ## Swift
    id_16 = BooleanField('หายใจเร็วกว่า25ครั้งต่อนาที')
    id_20 = BooleanField('ภาวะระบายลมหายใจเกิน (hyperventilation) ในผู้ป่วยที่เคยมีอาการเช่นนี้มาก่อน')
    id_5 = BooleanField('หายใจเร็ว แรง และลึก')

    ## Stuck
    id_6 = BooleanField('หายใจขัด')
    id_7 = BooleanField('พูด/หายใจขัด')
    id_8 = BooleanField('หายใจยากลำบาก')
    id_12 = BooleanField('ถูกควัน')
    id_9 = BooleanField('หายใจไม่พอ')
    id_14 = BooleanField('มีอาการ Airway Obstructuion')
    id_22 = BooleanField('คัด/แน่นจมูก')
    id_23 = BooleanField('อาการหวัดธรรมดา')

class ConciousnessForm(FlaskForm):
    conciousness = RadioField('ผู้ป่วยรู้สึกตัวหรือไม่', choices=[('concious', 'YES'), ('id_297', 'NO')], validators=[DataRequired()])
    # No
    id_335 = BooleanField('ไม่รู้สติ')
    id_336 = RadioField('พอปลุกตื่นได้หรือไม่', choices=[('canwake', 'YES'), ('cannotwake', 'NO')])
    # ไม่รู้สติ
    noconcioussub = RadioField('สถานะ', choices=[('id_329', 'ยืนยันได้ว่า ไม่รู้สติ'), ('id_330', 'ไม่ยืนยันการหมดสติ'), ('id_333', 'ไม่ตอบสนอง')])
    # Yes
    id_331 = BooleanField('รู้สึกตัวดี')
    id_337 = BooleanField('สภาพการรู้สติลดลงชัดเจน')
    id_327 = BooleanField('สูญเสียการรับความรู้สึก (ชา)')
    id_307 = BooleanField('ตื่นตระหนก, ไม่ทราบว่าเคยเป็นมาก่อน')
    id_308 = BooleanField('มีอาการเพ้อคลุ้มคลั่ง/เพ้อตื่นเต้น')
    hangover = RadioField('มีอาการมึนเมาจากสาเหตุเหล่านี้หรือไม่', choices=[('alcohol', 'เมาสุรา'), ('id_314', 'เมาสารเสพติด (เมายา)'), ('both', 'เมาสุราและใช้ยาเสพติดร่วมด้วย')])

    # เมา
    alcohol_ = RadioField('ลักษณะอาการ', choices=[('id_313', 'ตอบสนองต่อสิ่งเร้าได้'), ('id_312', 'ระดับความรู้สึกตัวลดลง'), ('alc_309', 'เมาสุราเฉียบพลันไม่ตอบสนองต่อสิ่งเร้า')]) # 309 check age
    alc_drg = RadioField('ลักษณะอาการ', choices=[('id_311', 'ตอบสนองต่อสิ่งเร้าได้'), ('id_310', 'เมาสุราเฉียบพลัน กินยาอื่นร่วมด้วย'), ('id_333', 'ไม่ตอบสนอง')])

    # รู้สึกตัวดี
    ## ปวด
    id_289 = BooleanField('ปวดท้อง')
    headache = BooleanField('ปวดศีรษะ')
    backache = BooleanField('ปวดหลัง') # มี 3 อายุ
    id_317 = BooleanField('ปวดอุ้งเชิงกราน')

    ### ปวดท้อง เช็คอายุก่อน
    lo_tummy = BooleanField('ปวดท้องส่วนล่าง') # มี 2 อายุ
    stomachache = BooleanField('ปวดกระเพาะอาหาร') # มี 3 อายุ
    stomachhurt = RadioField('มีอาการจุกเสียดหรือไม่', choices=[('id_253', 'ปวดจุกเสียดลิ้นปี่'), ('id_254', 'ปวดจุกเสียดท้องส่วนบน'), ('none', 'ไม่มีอาการจุกเสียด')]) # check age

    ### ปวดหัว
    id_305 = BooleanField('ปวดศีรษะรุนแรงเกิดขึ้นฉับพลัน')
    id_306 = BooleanField('ปวดศีรษะหลังการบาดเจ็บศีรษะ')
    id_328 = BooleanField('ปวดศีรษะรุนแรงไม่ใช่ไมเกรน')
    id_319 = BooleanField('ปวดศีรษะรุนแรง ก่อนมีอาการชัก')

   

    ##  เจ็บ
    chestache = BooleanField('เจ็บทรวงอก') 
    id_303 = BooleanField('เจ็บศีรษะ/ใบหน้า/ลำคอเล็กน้อย')
    id_304 = BooleanField('เจ็บตา,หู,จมูก,คอหอย')
    id_320 = BooleanField('เจ็บปวดทั่วๆ ร่างกาย')
    id_316 = BooleanField('บาดเจ็บช่องท้อง')
    id_344 = BooleanField('เจ็บปวดสะโพก')
    id_322 = BooleanField('เจ็บคอหอย')
    
    ### เจ็บทรวงอก เช็คอายุ
    id_229 = BooleanField('แน่นหน้าอก')
    chestpain = BooleanField('จุกเสียดยอดอก/ลิ้นปี่') # age+gender
    chestheart = BooleanField('เจ็บแน่นทรวงอก/หัวใจ') # age+gender
    chestinjury = BooleanField('บาดเจ็บทรวงอก') # age+gender
    heartchest = BooleanField('เจ็บแน่นทรวงอก/ใจสั่น') # age
    

    ### อื่นๆ
    vision = RadioField('การมองเห็นเป็นอย่างไร', choices=[('id_301', 'มองเห็นยากลำบาก'), ('id_300', 'เห็นภาพมัว/ภาพซ้อน'), ('normal_vision', 'มองเห็นปกติ')])
    fever = RadioField('มีไข้หรือไม่', choices=[('havefever', 'YES'), ('nofever', 'NO')])
    id_26 = BooleanField('มีอาการคัน')
    id_25 = BooleanField('กลืนลำบาก')
    id_321 = BooleanField('คลื่นไส้')

    #### ไข้
    id_325 = BooleanField('หนาวสั่น')
    
    id_345 = BooleanField('ไข้สูง> 39 องศา >24 ชม.')
    id_339 = BooleanField('มีไข้ 4-7 วัน')
    id_342 = BooleanField('รู้สึกว่าเด็กไม่ค่อยสบาย') # เช็คอายุก่อนแสดงผล


class ConversationForm(FlaskForm):
    talk = RadioField('สามารถพูดคุยสื่อสารได้หรือไม่', choices=[('id_28', 'Yes'), ('id_27', 'No')])

    # No
    id_35 = BooleanField('วางหูโทรศัพท์/เงียบหายไป')

    # Yes
    id_30 = BooleanField('ตื่น/พูดคุยรู้เรื่อง')
    ## cantalk
    id_32 = BooleanField('ยังคงพูดและเดินได้')

    ## voice
    id_31 = BooleanField('พูดเสียงพร่า')
    id_36 = BooleanField('เสียงพูดผิดไปจากปกติ')

    ## hardtotalk (id_39)
    id_38 = BooleanField('พูดไม่ชัด')
    id_37 = BooleanField('พูดไม่ปะติดปะต่อ/พูดลำบาก') # id_40 ด้วย
    timeoftalk = IntegerField('มีอาการนานเท่าใด (ชั่วโมง)')
    id_34 = BooleanField('ตอบคำถามไม่ถูกต้อง') # id_41 check age and time


class MovementForm(FlaskForm):
    id_42 = BooleanField('กล้ามเนื้อเป็นตะคริวรุนแรง')
    id_43  = BooleanField('อ่อนแรง/แขนขาไม่มีแรง/อัมพาต')
    id_44  = BooleanField('ต่อสู้ขัดขืนอย่างไร้เหตุผล')
    id_45  = BooleanField('ฆ่าตัวตายด้วยการยิง,แทง,บดทับ')
    id_46  = BooleanField('ตะคริว')
    id_47  = BooleanField('การทรงตัวผิดปกติ')
    id_49  = BooleanField('หน้าเบี้ยวเมื่อยิ้มหรือยิงฟัน')
    id_50  = BooleanField('ยกแขนทั้งสองข้างได้ไม่เท่ากัน')
    id_51  = BooleanField('แรงบีบมือทั้งสองข้าไม่เท่ากัน')
    id_52  = BooleanField('กำลังกล้ามเนื้ออ่อนแรง')
    id_53  = BooleanField('ยืนหรือเดินไม่ได้')
    paralyze = RadioField('มีอาการอัมพาตหรือไม่',choices=[('paralazed','Yes'),('notparalyzed','No')]) # age and time check 
    timeparalyzed = IntegerField('มีอาการอัมพาตเป็นเวลานานเท่าไหร่ (ชั่วโมง)')

class AppearanceForm(FlaskForm):
    # Shock and Severe Bleeding
    id_55 = BooleanField ('ซีดและเหงื่อท่วมตัว (Pale and sweating profusely)')
    id_56 = BooleanField('เหงื่อท่วมตัว (Profusely sweating)')
    id_57 = BooleanField('ซีดและผิวเย็นชืด (Pale and clammy skin)')
    id_58 = BooleanField('อาเจียนเป็นเลือดสด (Vomiting fresh blood)')
    id_60 = BooleanField('ถ่ายอุจจาระดำ (Black stool)')
    id_73 = BooleanField('เลือดออกห้ามไม่หยุด (Uncontrolled bleeding)')
    id_74 = BooleanField('เลือดออกนอกบริเวณที่ถูกกัด (Bleeding outside the bitten area)')
    id_78 = BooleanField('มีเลือดในปัสสาวะ (Blood in urine)')
    id_79 = BooleanField('ไอเป็นเลือด (Coughing blood)')
    id_80 = BooleanField('ภาวะเลือดออกไม่รหัสแดง (Non-red code bleeding)')
    id_81 = BooleanField('เลือดกำเดาไหล (Nosebleed)')
    id_87 = BooleanField('เครื่องกระตุกหัวใจอัตโนมัติช็อก (AED shock)')
    id_88 = BooleanField('มีอาการเขียวคล้ำ (Cyanosis)')
    id_90 = BooleanField('ลำตัว/ริมฝีปากเขียวคล้ำ (Cyanosis on body/lips)')
    id_89 = BooleanField('ชัก (Seizure)')
    id_117 = BooleanField('มีอาการแสดงช็อก (Shock symptoms)')

    # Allergic Reactions

    id_63 = BooleanField('คอหอยบวม (Swollen throat)')
    id_64 = BooleanField('ลิ้นบวม (Swollen tongue)')
    id_65 = BooleanField('ปฏิกิริยาต่อยา (Drug reaction)')
    id_66 = BooleanField('คิดถึงการแพ้ แต่ไม่เคยมีประวัติ (Suspected allergy without history)')
    id_67 = BooleanField('ลมพิษ (Hives)')
    id_68 = BooleanField('(ภูมิแพ้)เกิดขึ้นในเวลา>30น. (Allergy occurring in >30 mins)')

    # Animal and Insect Bites
    id_69 = BooleanField('ถูกสัตว์พิษร้ายแรงกัด> 10จุด (Severe animal bites >10 points)')
    id_70 = BooleanField('ถูกสัตว์ไม่มีพิษกัด ต่ำกว่าลำคอ (Non-venomous animal bite below neck)')
    id_71 = BooleanField('ถูกสัตว์กัด / เลีย / สัมผัส แต่ไม่มีอาการผิดปกติ (Animal bite/lick/touch without symptoms)')
    id_72 = BooleanField('ถูกกัดที่ลำคอ / ใบหน้า (Bite on neck/face)')
    id_76 = BooleanField('บวม/ฟกช้ำบริเวณที่ถูกกัด (Swelling/bruising at bite site)')

    # Environmental Exposure
    id_91 = BooleanField('ออกกำลังกายหนัก (Intense exercise)')
    id_92 = BooleanField('อยู่ในที่ร้อนจัดและมีเลือดออกผิดปกติ (In extreme heat with abnormal bleeding)')
    id_93 = BooleanField('อยู่ในที่ร้อนจัดและตัวร้อนจัด (In extreme heat and very hot)')
    id_94 = BooleanField('ไม่มีเหงื่อออก (No sweating)')
    id_95 = BooleanField('อาเจียน (Vomiting)')
    id_96 = BooleanField('อยู่ในที่ร้อนจัดและปัสสาวะ/อุจจาระราด (In extreme heat with incontinence)')
    id_97 = BooleanField('สารเคมี(กิน/ถูกราด/สาด/กระเด็น) (Chemical exposure)')
    id_98 = BooleanField('ถูกความเย็นจัด ควบคุมอาการสั่นไม่ได้ (Severe cold exposure, uncontrollable shaking)')
    id_99 = BooleanField('ภยันตรายอื่นๆ (Other dangers)')
    id_100 = BooleanField('ถูกภยันตรายอื่นแต่ไม่รุนแรง (Other non-severe dangers)')
    
    # Drug and Poison Exposure
    id_102 = BooleanField('ไมเกรน (Migraine)')
    id_105 = BooleanField('บาดเจ็บจากการทำร้ายตนเอง (Self-harm injury)')

    ## มีการกินยา/สารเคมี

    medicine = RadioField('ใช้ยาบำบัด', choices=[('med_taken', 'Yes'), ('med_not_taken', 'No')]) # id_106-107 timetaken check
    timetaken = IntegerField('ใช้ยาไปแล้วกี่ชั่วโมง')
    self_med = RadioField('การกินยา', choices=[('id_108', 'เจตนา,ด้วยยาสามัญประจำบ้าน (Intentional, with over-the-counter medication)'),
                                                          ('id_110', 'กินยาเกินขนาดแต่ผู้ป่วยปฏิเสธ (Overdose but patient denies)'),
                                                          ('id_111','กินยาเกินขนาดไม่ทราบว่าเกินไหม (Overdose uncertain)'), 
                                                          ('id_114', 'มีอาการผิดปกติจากการใช้ยา (Adverse drug reaction)'),
                                                          ('id_115', 'ไม่มีอาการผิดปกติใด, แต่ได้รับยา (No symptoms, but took medication)')])
    id_112 = BooleanField('สารเคมี (กินเข้าไป หรือ ถูกสาด) (Chemical ingestion/splash)')
    id_189 = BooleanField('สารเคมีไหม้ตา (Chemical eye burn)')
    corrosive = BooleanField('กินสารกัดกร่อน (Ingested corrosive)')
    ###
    swoll = RadioField('มีอาการกลืนลำบากหรือไม่', choices=[('id_109', 'Yes'), ('id_145', 'No')])
    
    ### id_114 checked
    adverse = RadioField('ทราบชนิดของยาหรือไม่', choices=[('drugknown', 'Yes'), ('id_113', 'No')])
    drug_type = StringField('ชนิดของยา')

    ### id_110 or id_111 checked
    tekentime = IntegerField('ได้รับยาเกินขนาดมาแล้วกี่นาที') # id_149 < 30 / id_151 > 30


    # มีอาการชัก
    id_104 = BooleanField('ชักตามหลังการบาดเจ็บ (Post-injury seizure)')
    id_116 = BooleanField('ชัก,จากAlc./ยาเกินขนาด/ถอนยา (Seizure from alcohol/overdose/withdrawal)')
    id_126 = BooleanField('กำลังชัก(>5 นาที) (Seizure >5 mins)')
    id_127 = BooleanField('ชัก>3ครั้งต่อชม. (Seizure >3 times/hour)')
    id_128 = BooleanField('ชักหลังบาดเจ็บศีรษะภายใน24ชม. (Seizure post head injury within 24 hrs)')
    id_130 = BooleanField('ชักครั้งแรกในชีวิต (First seizure in life)')
    id_131 = BooleanField('ชัก (ไม่ทราบว่าเคยชักมาก่อนหรือไม่) (Seizure, unknown history)')
    id_132 = BooleanField('ไม่มีอาการชักแต่มีสัญญาณบอกเหตุก่อนชัก (No seizure but pre-seizure signs)')
    id_133 = BooleanField('ชัก ในผู้ที่มีประวัติเคยชักมาก่อน (Seizure in known epileptic)')
    id_143 = BooleanField('ชัก เข้าไม่ได้กับ ‘รหัสแดง’ (Seizure, not red code)')
    id_205 = BooleanField('ชักตามหลังบาดเจ็บศีรษะ (Seizure post head injury)') # id_208 headtime check
    headtime = IntegerField('ชักหลังบาดเจ็บศีรษะเป็นเวลา (ชั่วโมง)') 
    
    
    # Injuries and Trauma
    id_29 = BooleanField('มีพฤติกรรมต่างจากที่เคยเป็น (Behavior changes from usual)')
    id_152 = BooleanField('เงื่องหงอย เซื่องซึม (Lethargic, sluggish)')
    id_153 = BooleanField('ตัวอ่อนปวกเปียก (Floppy body)')
    id_141 = BooleanField('ฟุบอยู่กับพวงมาลัยยานพาหนะ (Slumped at the steering wheel)')
    id_158 = BooleanField('เลือดออกผิดปกติ,ไม่ได้รับบาดเจ็บ (Abnormal bleeding, no injury)')
    id_159 = BooleanField('ตัวซีดเย็น (Pale and cold)')
    id_206 = BooleanField('หายใจได้ตามปกติ,แต่มีการบาดเจ็บที่ช่องปาก (Normal breathing but oral injury)')
    id_134 = BooleanField('ไอ (Cough)')
    id_200 = BooleanField('ดวงตาแดงมาก (Very red eyes)')
    id_182 = BooleanField('วิตกกังวลแต่ไม่ปรากฏการบาดเจ็บ (Anxiety without apparent injury)')

    id_62 = BooleanField('ปวดร่วมกับอาเจียน (Pain with vomiting)')
    id_160 = BooleanField('อาการขาดสารน้ำ (Dehydration)')
    id_161 = BooleanField('อาเจียน/ถ่ายเหลว > 10 ครั้งต่อวัน (Vomiting/diarrhea >10 times/day)')

    id_59 = BooleanField('บาดเจ็บขาหนีบ (Groin injury)')
    id_103 = BooleanField('มีอาการตามหลังการบาดเจ็บ (Post-injury symptoms)')
    id_118 = BooleanField('บาดเจ็บจากการทำร้ายตนเอง (Self-harm injury)')
    id_142 = BooleanField('มีการบาดเจ็บเล็กน้อย (Minor injury)')
    id_163 = BooleanField('กรีดร้องโหยหวน (Screaming in agony)')
    id_165 = BooleanField('ถูกยิงหรือถูกแทง (Gunshot or stab wound)')
    id_168 = BooleanField('ถูกบดหรือมีบาดแผลเจาะทะลุที่มือหรือเท้า (Crushed/puncture wound on hand/foot)')
    id_171 = BooleanField('แขนขาหักหลายแห่ง (Multiple fractures in limbs)')
    id_172 = BooleanField('กระดูกต้นขาหัก (Femur fracture)')
    id_174 = BooleanField('บาดเจ็บไม่ทราบสาเหตุ (Injury of unknown cause)')
    id_175 = BooleanField('ฟกช้ำ/บาดเจ็บเล็กน้อย,ไม่ใช่อาวุธ (Minor bruise/injury, not a weapon)')
    id_176 = BooleanField('แผลฉีกขาดที่ห้ามเลือดให้หยุดได้ (Controlled laceration bleeding)')
    id_177 = BooleanField('กระดูกหัก/เคลื่อน(แขน/ขา) (Fracture/dislocation of arm/leg)')
    id_178 = BooleanField('กระดูกหัก/เคลื่อน(นิ้วมือ/นิ้วเท้า) (Fracture/dislocation of fingers/toes)')
    id_180 = BooleanField('บาดเจ็บศีรษะ/ลำคอเล็กน้อย (Minor head/neck injury)')
    id_203 = BooleanField('ศีรษะบาดเจ็บระดับเล็กน้อยถึงปานกลาง (Mild to moderate head injury)')
    id_204 = BooleanField('ถูกตีหัว/ฟาด/ล้มโดนศีรษะ,ยกเว้นข้อ 202-203 (Hit head/fell, except codes 202-203)')
    
    id_137 = BooleanField('เมาสุราเฉียบพลัน (Acute alcohol intoxication)')
    id_138 = BooleanField('เมาสุรา (Alcohol intoxication)')
    id_156 = BooleanField('ดื่มแอลกอฮอล์ร่วมกับใช้ยา (Alcohol with drug use)')

    id_187 = BooleanField('ถูกช็อตจากสายไฟโดยตรง/กล่องจ่ายไฟฟ้า (Direct electric shock)')
    
    id_198 = BooleanField('จมน้ำ/หน้าคว่ำในน้ำ (Drowning/face down in water)')
    id_199 = BooleanField('เกือบจมน้ำ,ไม่ปรากฏการบาดเจ็บ (Near-drowning without apparent injury)')
    
    # Cardiac and Respiratory Conditions
    HR = IntegerField('Heart Rate') 
    # id_240 = BooleanField('HR>100 PR>20 อายุ> 8ปี (HR >100 PR >20 Age >8 years)')
    # id_241 = BooleanField('HR>140 PR>30 อายุ3-8ปี (HR >140 PR >30 Age 3-8 years)')
    
    # Pediatric Conditions
    id_82 = BooleanField('อาการไอคล้ายเห่า(Barking cough)') #  อายุ <= 6 
    DOA = BooleanField('Dead on arrival + ตัวเย็น/แข็ง') 
    # id_83 = BooleanField('DOA ตัวเย็น/แข็ง อายุ <1 ปี (DOA cold/stiff, Age <1 year)')
    # id_84 = BooleanField('DOA ตัวเย็น/แข็ง อายุ >=1 ปี (DOA cold/stiff, Age ≥1 year)')

class CongenitialDiseaseForm(FlaskForm):
    id_349 = BooleanField ('เคยมีประวัติช็อคภูมิแพ้ เกิดใน30นาทีหลังรับสิ่งที่แพ้')
    id_350 = BooleanField ('ประวัติเคยมีปฏิกิริยาภูมิแพ้(อดีต)')
    id_351 = BooleanField ('ผู้ป่วยขาดยาทางจิตเวชกรรม')
    id_352 = BooleanField ('เบาหวาน')
    id_353 = BooleanField ('ภาวะผิดปกติแต่กำเนิดที่มีอันตรายต่อชีวิต')
    id_354 = BooleanField ('ภาวะผิดปกติแต่กำเนิด')
    id_355 = BooleanField ('ตรวจพบเชื้อไวรัสโคโรนา 2019')
    id_356 = BooleanField ('ปัญหาสายสวนปัสสาวะ')

class OtherForm(FlaskForm):
    id_33 = BooleanField('ผู้ป่วยยืนยันขอให้ช่วย')
    id_357 = BooleanField('ผู้แจ้งตรวจสอบยืนยันรายละเอียดอาการของผู้ป่วยไม่ได้')
    id_358 = BooleanField('บุคคลที่ทำหนังสือแสดงเจตนาไม่ประสงค์จะรับบริการสาธารณสุขที่เป็นไปเพียงเพื่อยืดการตายในวาระสุดท้ายของชีวิตตน หรือเพื่อยุติการทรมานจากการเจ็บป่วย ')
    id_359 = BooleanField('อาการไม่จำเพาะ')
    id_360 = BooleanField('ไม่ได้ข้อมูลยืนยันจากผู้แจ้ง')
    id_361 = BooleanField('ตำรวจ/เจ้าหน้าที่ระงับภัยร้องขอ')
    id_362 = BooleanField('ผู้แจ้งยืนยันขอให้ช่วย')
    id_363 = BooleanField('องค์กรยืนยันภาวะฉุกเฉินการแพทย์')
    id_364 = BooleanField('อื่นๆที่พิจารณาว่าอาจวิกฤต')
    id_365 = BooleanField('องค์กรยืนยันภาวะไม่วิกฤต')
    id_366 = BooleanField('องค์กรยืนยันไม่มีรายละเอียด')
    id_367 = BooleanField('ความดันเลือดสูง ที่ไม่มีอาการจำเพาะ')
    id_368 = BooleanField('ผู้แจ้งร้องขอการประเมิน')
    id_369 = BooleanField('ตำรวจร้องขอตรวจสอบการบาดเจ็บ')
    id_370 = BooleanField('เกณฑ์อุบัติภัยหมู่')