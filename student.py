
from openerp.osv import fields,osv


class student_student(osv.osv):
    _name='student.student'
    _columns={
         'nom': fields.char('Nom', size=64, required=True),
         'prenom': fields.char('Prenom', size=64, required=True),
         'cin': fields.integer('CIN', size=8, required=True),
         'datenaiss': fields.date('Date Naissance',required=True),
         'departement_id':fields.many2one('student.departement','Departement',required=True),

    }
student_student()

class student_departement(osv.osv):
    _name='student.departement'

    def _get_student(self, cr, uid, ids, name, arg, context=None):
        res =  {}
        for id in ids:
            res[id] ={'tot_student':0.0}
            cr.execute('SELECT COALESCE(COUNT(*), 0) as tot_student  FROM student_student WHERE departement_id = %s', (id,))
            lines = cr.dictfetchall()
            for l in lines:
                res[id]['tot_student'] = l['tot_student']
        return res

    _rec_name='designation'
    _columns={
         'code': fields.char('Code', size=3, required=True,select=True),
         'designation': fields.char('Designation', size=64, required=True),
         'student_ids':fields.one2many('student.student','departement_id','Liste Etudiant',readonly=True),       
         'tot_student': fields.function(_get_student,multi="progress", string="Student Number"),
    }
student_departement()

class student_club(osv.osv):
    _name='student.club'
    _rec_name='designation'
    _columns={
         'code': fields.char('Code', size=3, required=True,select=True),
         'designation': fields.char('Designation', size=64, required=True),
         'student_ids':fields.many2many('student.student',string='Liste Etudiant'),       
    }
student_club()
