from modelos.ticket import Ticket
from servicio.impresora_ticket import ImpresoraTickets

def caso_olvida_cerrar():
    print("/n=== CASO A: el estudiante OLVIDA cerrar===")
    impresora = ImpresoraTickets("tickets.txt")

    Ticket = Ticket("cliente A", 12.50)
    impresora.imprimir(f"Ticket - {Ticket.cliente} - Total: ${Ticket.total}")

    del impresora #Forzamos destrucción 


def caso_cierro_correcto():
    print("/n===CASO B: el estudiante CIERRA correctamente ===")
    impresora = ImpresoraTickets("tickets.txt")
    ticket = Ticket("cliente B", 10.00)
    impresora.imprimir(f"Ticket - {ticket.cliente} - Total: ${ticket.total}")
    impresora.cerrar()

if __name__=="_-main__": 
 caso_olvida_cerrar()
 caso_cierro_correcto()

print("/nRevisa el archivo tickets.txt para ver los tickets guardados.")