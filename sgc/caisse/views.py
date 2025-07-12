from django.shortcuts import render, redirect
from django.contrib import messages
from sgc.service_factory import get_caisse_service
from sgc.core.models import LigneVente, Magasin

def vue_rechercher_produit(request):
    print("Recherche de produit avec critères :", request.GET)
    caisse_service = get_caisse_service()

    critere_nom = request.GET.get('nom', '')
    critere_cat = request.GET.get('categorie', '')
    critere_id = request.GET.get('id', '')

    criteria = {
        'nom': critere_nom,
        'categorie': critere_cat,
        'id': critere_id
    }

    produits = caisse_service.rechercher_produits(criteria)

    if produits:
        print(f"🟢 {len(produits)} produit(s) trouvé(s) :")
        for produit in produits:
            print(f" - {produit}")
    else:
        print("🔴 Aucun produit trouvé.")

    return render(request, 'caisse/produits.html', {
        'produits': produits,
        'criteres': criteria
    })


def vue_enregistrer_vente(request):
    caisse_service = get_caisse_service()

    if request.method == "POST":
        try:
            ids_str = request.POST.get("produits", "")
            ids = [int(pid.strip()) for pid in ids_str.split(",") if pid.strip().isdigit()]

            # Construire les lignes de vente
            lignes = []
            for pid in ids:
                produit = caisse_service.rechercher_produits({'id': pid})[0]
                if not produit:
                    raise Exception(f"Produit avec ID {pid} introuvable.")
                else:
                    lignes.append(LigneVente(produit=produit, quantite=1))

            magasin = Magasin.objects.first()

            vente = caisse_service.enregistrer_vente(lignes, magasin)

            return render(request, "caisse/confirmation_vente.html", {"total": vente["total"]})

        except Exception as e:
            messages.error(request, str(e))

    return render(request, "caisse/vente.html")

def vue_gestion_retour(request):
    if request.method == 'POST':
        # Traiter le retour via VenteService
        pass
    return render(request, 'caisse/retour.html')

def vue_stock_magasin(request):
    # Appeler StockService pour afficher le stock local
    return render(request, 'caisse/stock_magasin.html')

def vue_stock_central(request):
    # Appeler StockService pour afficher le stock central
    return render(request, 'caisse/stock_central.html')

def vue_demande_approvisionnement(request):
    if request.method == 'POST':
        # Initier une demande via DemandeApprovisionnementService
        pass
    return render(request, 'caisse/demande_approvisionnement.html')
