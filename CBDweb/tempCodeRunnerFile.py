

        if form.id_369.data:
            output_dict['id_369'] = 1
        else:
            pass

        if form.id_370.data:
            output_dict['id_370'] = 1
        else:
            pass




        process_output_data(session['output_dict'])
        return redirect(url_for('other_page'))