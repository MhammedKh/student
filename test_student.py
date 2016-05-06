# -*- encoding: utf-8 -*-

from openerp.tests.common import TransactionCase


class test_student(TransactionCase):
    def setUp(self):
        super(test_student, self).setUp()
        
		self.student_ids = self.registry("student.student")
		self.departement = self.registry("student.departement")

    def test_create(self):
        cr, uid = self.cr, self.uid
		self.assertEquals(100, self.student_ids)
