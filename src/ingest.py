from src.chunker import manual_ckunk_text
from src.client import supabase
from src.embeddings import get_embeddings

def add_large_document(text: str, source_name: str = "documento_prueba"):
    chunks = manual_ckunk_text(text, chunk_size=400, chunk_overlap=80)
    print(f"El texto fue dividido en {len(chunks)} chunks.")
    
    for i, chunk in enumerate(chunks):
        print(f"Generando embedding para chunk {i+1}/{len(chunks)}...")
        embedding = get_embeddings(chunk)
        
        supabase.table("documents")\
        .insert({
            "content":chunk,
            "metadata":{
                "source": source_name,
                "chunk_index": i,
                "total_chunks": len(chunks)
            },
            "embedding":embedding
        }).execute()

    print("Guardado en supabase con éxito.")

    
if __name__ == "__main__":
    add_large_document(
        """
         El café es una de las bebidas más consumidas en todo el mundo y su
  historia está llena de mitos fascinantes. Cuenta la leyenda que en el siglo
  IX, en las tierras altas de Etiopía, un pastor de cabras llamado Kaldi notó
  que su rebaño se comportaba con una energía inusual y no dormía por las
  noches después de comer las bayas rojas de un arbusto desconocido.
  Intrigado por este fenómeno, Kaldi llevó los frutos a un monje de un
  monasterio local, quien decidió hervirlas para crear una infusión amarga
  que permitía a los monjes mantenerse despiertos y concentrados durante las
  largas oraciones nocturnas.

    Desde África oriental, la planta del café cruzó el Mar Rojo hacia la
  península arábiga en el siglo XV. En Yemen se perfeccionó la técnica de
  tostar los granos y molerlos, dando origen al café tal como lo conocemos
  hoy en día. El puerto yemení de Moca se convirtió en el principal centro de
  comercio internacional de este codiciado grano, y las primeras cafeterías
  públicas, conocidas como 'qahveh khaneh', florecieron en ciudades como El
  Cairo, Damasco y Constantinopla como centros de encuentro social, debate
  político y juego de ajedrez.

    En la actualidad, existen dos especies principales de plantas de café que
  dominan el mercado global: Coffea Arabica y Coffea Robusta. El grano de
  Arábica representa aproximadamente el sesenta por ciento de la producción
  mundial, se cultiva a grandes alturas por encima de los novecientos metros
  sobre el nivel del mar y ofrece un perfil de sabor complejo, aromático y
  con acidez brillante. Por su parte, la variedad Robusta es más resistente a
  las plagas, crece a menores altitudes y contiene casi el doble de cafeína,
  aportando cuerpo denso y un característico amargor a las mezclas de
  espresso.

    Para preparar una taza perfecta, los baristas recomiendan mantener la
  temperatura del agua entre los noventa y los noventa y seis grados Celsius.
  Si el agua hierve y supera los noventa y siete grados, puede quemar los
  compuestos solubles del grano molido, provocando un sabor áspero y
  sobreextraído. Hoy en día, Brasil se posiciona como el mayor productor y
  exportador de café del planeta, seguido por Vietnam y Colombia.

        """
    )
    
