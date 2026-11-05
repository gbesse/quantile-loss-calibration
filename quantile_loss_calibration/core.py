import math,itertools
from .common import number,integer,identifier,unique_ids
def run(d):
 qs=[number(v,1e-9,1-1e-9)for v in d['quantiles']];rows=d['cases'];unique_ids(rows)
 if len(qs)!=len(set(qs))or qs!=sorted(qs)or not qs or len(qs)>100 or not 1<=len(rows)<=10000:raise ValueError('quantiles')
 losses=[0.0]*len(qs);covered=[0]*len(qs);cross=[]
 for r in rows:
  y=number(r['actual']);pred=[number(x)for x in r['predictions']]
  if len(pred)!=len(qs):raise ValueError('shape')
  violations=[i for i in range(len(pred)-1)if pred[i]>pred[i+1]]
  if violations:cross.append(dict(id=r['id'],crossing_between_indices=violations))
  for i,(q,p)in enumerate(zip(qs,pred)):
   err=y-p;losses[i]+=max(q*err,(q-1)*err);covered[i]+=y<=p
 return dict(quantiles=[dict(q=q,mean_pinball_loss=losses[i]/len(rows),empirical_fraction_at_or_below=covered[i]/len(rows),calibration_difference=covered[i]/len(rows)-q)for i,q in enumerate(qs)],crossing_cases=cross,cases=len(rows))
