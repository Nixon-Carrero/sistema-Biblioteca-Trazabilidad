from src.PrestamoService import PrestamoService



def test_tst_int_001_prestamo():

  srv = PrestamoService()

  p = srv.registrar_prestamo(1, "Ingeniería de Software")

  assert p.activo is True



def test_tst_int_002_devolucion():

  srv = PrestamoService()

  p = srv.registrar_prestamo(1, "Ingeniería de Software")

  srv.registrar_devolucion(p)

  assert p.activo is False



def test_tst_int_003_renovacion():

  srv = PrestamoService()

  p = srv.registrar_prestamo(1, "Ingeniería de Software")

  assert srv.renovar_prestamo(p) is True

  assert srv.renovar_prestamo(p) is False