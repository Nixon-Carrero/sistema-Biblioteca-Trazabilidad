class Prestamo:

  def __init__(self, id_prestamo, libro, activo=True):

    self.id_prestamo = id_prestamo

    self.libro = libro

    self.activo = activo

    self.renovaciones = 0



class PrestamoService:

  def registrar_prestamo(self, id_prestamo, libro):

    return Prestamo(id_prestamo, libro, activo=True)



  def registrar_devolucion(self, prestamo):

    prestamo.activo = False

    return prestamo



  def renovar_prestamo(self, prestamo):

    if prestamo.activo and prestamo.renovaciones < 1:

      prestamo.renovaciones += 1

      return True

    return False