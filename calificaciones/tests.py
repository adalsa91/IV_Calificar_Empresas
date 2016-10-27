#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from django.test import TestCase
from calificaciones.models import Empresa
from calificaciones.models import Alumno


class EmpresaMethodTests(TestCase):

    def test_empresa_creation(self):
        emp = Empresa(nombre='Prueba')
        emp.save()

        empresas = Empresa.objects.all()
        self.assertEqual(empresas.count(), 1)

        self.assertEqual(emp.nombre, 'Prueba')
        self.assertEqual(str(emp), emp.nombre)


class AlumnoMethodTests(TestCase):

    def test_alumno_creation(self):
        emp = Empresa(nombre='Prueba')
        emp.save()
        alum = Alumno(nombre='John', empresa=emp, puntuacion='8')
        alum.save()

        alumnos = Alumno.objects.all()
        self.assertEqual(alumnos.count(), 1)

        self.assertEqual(alum.nombre, 'John')
        self.assertEqual(alum.puntuacion, '8')
