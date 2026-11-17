class Prestamo:

  def __init__(self, id_prestamo, libro, activo=True):

    self.id_prestamo = id_prestamo

    self.libro = libro

    self.activo = activo



class PrestamoService:

  def registrar_prestamo(self, id_prestamo, libro):

    return Prestamo(id_prestamo, libro, activo=True)



  def registrar_devolucion(self, prestamo):

    prestamo.activo = False

    return prestamo