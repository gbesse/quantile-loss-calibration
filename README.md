# quantile-loss-calibration

## Français

Diagnostiquer les quantiles croisés et leur perte asymétrique.

Données fictives ; aucun accès réseau ni secret requis.

```sh
python -m quantile_loss_calibration examples/demo.json --lang fr
python -m unittest discover -s tests -v
```

### Méthode et différence

Perte pinball classique et fractions empiriques par quantile, avec détection des croisements avant toute correction. Compare pertes asymétriques et couverture observée.

### Limites

Diagnostic sur données fournies, sans estimation d’intervalle de confiance ni garantie de couverture future ; ne réordonne pas les prédictions utilisateur.

### Validation

Tests de domaine, cas limites et interface FR/EN/ES. La CI teste Python 3.11/3.13 et exécute la wheel installée hors du checkout. JSON conserve les identifiants techniques et les données fournis. Erreur d’entrée : code de sortie 2.

## English

Diagnose crossing quantiles and asymmetric loss.

Synthetic data; no network access or secret required.

```sh
python -m quantile_loss_calibration examples/demo.json --lang en
python -m unittest discover -s tests -v
```

### Method and difference

Classical pinball loss and empirical fractions by quantile, with crossing detection before any correction. Compares asymmetric losses and observed coverage.

### Limits

Diagnostic on supplied data without confidence intervals or future-coverage guarantee; does not reorder user predictions.

### Validation

Domain tests, boundary cases and FR/EN/ES interface. CI tests Python 3.11/3.13 and runs the installed wheel outside the checkout. JSON preserves technical identifiers and supplied data. Invalid input exits with code 2.

## Español

Diagnosticar cuantiles cruzados y pérdida asimétrica.

Datos sintéticos; no requiere red ni secretos.

```sh
python -m quantile_loss_calibration examples/demo.json --lang es
python -m unittest discover -s tests -v
```

### Método y diferencia

Pérdida pinball clásica y fracciones empíricas por cuantil, detectando cruces antes de corregir. Compara pérdidas asimétricas y cobertura observada.

### Límites

Diagnóstico sobre datos aportados sin intervalos de confianza ni garantía de cobertura futura; no reordena predicciones del usuario.

### Validación

Pruebas de dominio, casos límite e interfaz FR/EN/ES. CI prueba Python 3.11/3.13 y ejecuta la wheel instalada fuera del repositorio. JSON conserva identificadores técnicos y datos proporcionados. Entrada inválida termina con código 2.

## Sources / Fuentes

- https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_pinball_loss.html
