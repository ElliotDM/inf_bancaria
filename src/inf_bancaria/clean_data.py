def remove_columns(df):
    """
    Processes the data frame removing 
    unnecessary columns for the project.
    """
    columns = ['NUM_SOLICITUD', 'SUCURSAL', 'STATUS_SOLICITUD', 'PUNTO_DECISION',
       'APROBACION_TC', 'LINEA_CREDITO_FINAL', 'CUENTA_ASIGNADA',
       'SALDO_CUENTA', 'CAPACIDAD_TC', 'COMPROBANTE_INGRESOS', 
       'SEGMENTO_CLIENTE', 'CLIENTE_CDE', 'SUMA_LINEAS_REVOLVENTES', 
       'CAPACIDAD_PAGO_TOTAL','PEOR_MOP_TARJETAS', 'SUMA_SALDOS_TARJETAS', 
       'SUMA_PAGO_MIN_TARJETAS', 'PEOR_HISTORIA_CREDITO', 'SUMA_SALDOS_TOTAL', 
       'NUM_CREDITOS',]
    
    return df.drop(columns, axis=1)
