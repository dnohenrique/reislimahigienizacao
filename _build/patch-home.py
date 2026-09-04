# -*- coding: utf-8 -*-
"""Aplica os ajustes de SEO on-page na index.html (home). Idempotente."""
import os, re, sys
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
g = {"__file__": os.path.join(RAIZ, "_build", "gerar-paginas.py")}
exec(open(os.path.join(RAIZ, "_build", "gerar-paginas.py"), encoding="utf-8").read().split('if __name__')[0], g)
SERVICOS, REGIOES = g["SERVICOS"], g["REGIOES"]
SITE, NOME, TEL1, TEL2, TEL1_R, TEL2_R = g["SITE"], g["NOME"], g["TEL1"], g["TEL2"], g["TEL1_R"], g["TEL2_R"]
EMAIL, CNPJ, zap = g["EMAIL"], g["CNPJ"], g["zap"]

p = os.path.join(RAIZ, "index.html")
h = open(p, encoding="utf-8").read()
orig = h
def sub(a, b, obrig=True):
    global h
    if a not in h:
        if obrig and b not in h: sys.exit("NAO ENCONTRADO: " + a[:80])
        return
    h = h.replace(a, b, 1)

# 1. idioma
sub('<html>\n<head>', '<html lang="pt-BR">\n<head>')

# 2. title unico e mais comercial
sub('<title>Estofados, Colchões e Vidros em São Paulo | Reis Lima Higienização </title>',
    '<title>Higienização de Estofados e Vidros em São Paulo | Reis Lima</title>')

# 3. metas extras
sub('<meta name="robots" content="index, follow" />',
    '<meta name="robots" content="index, follow, max-image-preview:large" />\n'
    '<meta name="geo.region" content="BR-SP" />\n'
    '<meta name="geo.placename" content="São Paulo" />')

# 4. JSON-LD (negocio local + FAQ + site) antes do </helmet>
FAQ_HOME = [
 ("Quais regiões vocês atendem?","Atendemos São Paulo e região, incluindo Zona Sul, Zona Oeste, Zona Norte, Centro e o ABC Paulista. Envie o endereço pelo WhatsApp e confirmamos a disponibilidade."),
 ("Qual é o horário de atendimento?","Nosso atendimento é de segunda a sábado, das 8h às 19h. O agendamento do serviço é feito no horário mais conveniente para você dentro desse período."),
 ("Como é feito o orçamento?","O orçamento é gratuito e sem compromisso. Basta informar o tipo de serviço, a quantidade de peças ou a metragem e, se possível, enviar fotos pelo WhatsApp."),
 ("Quanto tempo o estofado leva para secar?","O tempo varia conforme o tecido, a ventilação e o clima do dia. Usamos processo de extração que reduz bastante a umidade e orientamos você sobre os cuidados até a secagem completa."),
 ("Vocês atendem empresas e condomínios?","Sim. Atendemos comércios, escritórios e condomínios, inclusive em contratos de manutenção periódica de estofados, vidros e fachadas."),
 ("Quanto custa a higienização de um sofá?","O valor depende do número de lugares, do tipo de tecido e do estado do estofado. Envie uma foto pelo WhatsApp e enviamos o preço fechado, sem compromisso."),
]
site_ld = ('{"@context":"https://schema.org","@type":"WebSite","name":"%s","url":"%s/",'
           '"inLanguage":"pt-BR","publisher":{"@id":"%s/#negocio"}}' % (NOME, SITE, SITE))
ld = '[' + g["ld_negocio"](SITE + "/") + ',' + g["ld_faq"](FAQ_HOME) + ',' + site_ld + ']'
if 'application/ld+json' not in h:
    sub('</helmet>', '<script type="application/ld+json">' + ld + '</script>\n</helmet>')

# 5. cards de servico viram links para as paginas dedicadas
MAPA = {
 "Limpeza e cristalização de vidros e fachadas":"cristalizacao-de-vidros",
 "Higienização de sofás":"higienizacao-de-estofados",
 "Higienização de colchões":"higienizacao-de-colchoes",
 "Higienização de cadeiras":"higienizacao-de-cadeiras",
 "Higienização de tapetes":"limpeza-de-tapetes",
 "Impermeabilização de estofados":"impermeabilizacao-de-estofados",
}
for texto, slug in MAPA.items():
    velho = '; padding-top:8px">' + texto + '</h3>'
    novo = '; padding-top:8px"><a href="/%s/" style="color:#003366">%s</a></h3>' % (slug, texto)
    if velho in h: h = h.replace(velho, novo, 1)
    elif novo not in h: sys.exit("card nao encontrado: " + texto)

# 6. card novo de fachadas + linha "ver pagina" nos cards
ancora = 'prolongando a vida útil do seu estofado.</p>\n        </div>'
card_fachada = ancora + """
        <div style="background:#FFFFFF; border:1px solid #DFE3E6; border-radius:20px; padding:32px 28px 30px; display:flex; flex-direction:column; gap:12px; transition:transform 0.22s ease, box-shadow 0.22s ease" style-hover="transform:translateY(-6px); box-shadow:0 18px 40px rgba(0,114,255,0.12)">
          <span style="width:38px; height:4px; border-radius:99px; background:linear-gradient(90deg,#00C6FF,#0072FF)"></span>
          <h3 style="font-size:clamp(18px,2.1vw,21px); font-weight:700; color:#003366; padding-top:8px"><a href="/limpeza-de-fachadas/" style="color:#003366">Limpeza de fachadas de vidro</a></h3>
          <p style="font-size:15px; line-height:1.65; color:#5B6B79">Fachadas envidraçadas de prédios, lojas e condomínios, com limpeza pós-obra e cristalização opcional.</p>
        </div>"""
if 'limpeza-de-fachadas/' not in h.split('<footer')[0]:
    sub(ancora, card_fachada)

# 7. secao de regioes atendidas antes do FAQ
chips = "".join('<a href="/%s/" style="display:inline-block; font-size:15px; font-weight:600; color:#003366; background:#FFFFFF; border:1px solid #DFE3E6; border-radius:999px; padding:11px 20px; margin:0 10px 10px 0">%s</a>' % (r["slug"], r["menu"]) for r in REGIOES)
sec_reg = """  <section id="regioes" style="background:#FFFFFF; border-top:1px solid #E4E7E9">
    <div style="max-width:1200px; margin:0 auto; padding:clamp(50px,7vw,84px) clamp(16px,4vw,28px)">
      <div style="display:flex; flex-direction:column; gap:14px; max-width:680px; margin-bottom:26px">
        <span style="font-size:13px; font-weight:700; letter-spacing:0.12em; text-transform:uppercase; color:#00C6FF">Onde atendemos</span>
        <h2 style="font-size:clamp(25px,4.4vw,40px); line-height:1.12; font-weight:800; color:#003366">Higienização em toda São Paulo e região</h2>
        <p style="font-size:clamp(15.5px,1.7vw,17px); line-height:1.65; color:#5B6B79">Atendemos a capital, a Grande São Paulo e o ABC Paulista. Veja a página da sua região e peça o orçamento pelo WhatsApp.</p>
      </div>
      <div>%s</div>
    </div>
  </section>

""" % chips
if 'id="regioes"' not in h:
    sub('  <section id="faq"', sec_reg + '  <section id="faq"')

# 8. rodape: servicos reais, regioes e NAP completo
ini = h.find('>Serviços</span>', h.find('<footer'))
fim = h.find('<span style="font-size:14.5px">Atendimento das 8h às 19h</span>')
if ini == -1 or fim == -1: sys.exit("rodape nao encontrado")
if '/higienizacao-de-colchoes/' not in h[ini:fim]:
    ls = "".join('\n        <a href="/%s/" style="font-size:14.5px; color:#9FD3EA">%s</a>' % (s["slug"], s["menu"]) for s in SERVICOS)
    lr = "".join('\n        <a href="/%s/" style="font-size:14.5px; color:#9FD3EA">%s</a>' % (r["slug"], r["menu"]) for r in REGIOES)
    novo = ('>Serviços</span>' + ls +
      '\n      </div>\n      <div style="display:flex; flex-direction:column; gap:12px">'
      '\n        <span style="font-family:\'Plus Jakarta Sans\'; font-size:15px; font-weight:700; color:#FFFFFF">Regiões atendidas</span>' + lr +
      '\n      </div>\n      <div style="display:flex; flex-direction:column; gap:12px">'
      '\n        <span style="font-family:\'Plus Jakarta Sans\'; font-size:15px; font-weight:700; color:#FFFFFF">Contato</span>'
      '\n        <a href="%s" target="_blank" rel="noopener" style="font-size:14.5px; color:#9FD3EA">WhatsApp %s</a>'
      '\n        <a href="tel:%s" style="font-size:14.5px; color:#9FD3EA">Telefone %s</a>'
      '\n        <a href="mailto:%s" style="font-size:14.5px; color:#9FD3EA">%s</a>'
      '\n        <span style="font-size:14.5px; line-height:1.6">São Paulo — SP<br />Capital, Grande SP e ABC</span>'
      '\n        <span style="font-size:14.5px">CNPJ %s</span>'
      '\n        ') % (zap("Olá! Gostaria de um orçamento."), TEL1, TEL2_R, TEL2, EMAIL, EMAIL, CNPJ)
    h = h[:ini] + novo + h[fim:]

open(p, "w", encoding="utf-8").write(h)
print("index.html atualizada." if h != orig else "index.html ja estava atualizada.")
