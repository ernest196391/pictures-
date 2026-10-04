"""Read-only preflight: reuse approved assets before scheduling generation."""
import argparse
import hashlib
import json
from pathlib import Path


def check_batch(batch, store):
    manifest = json.loads((batch / 'manifest.json').read_text())
    products = json.loads((batch / 'products.json').read_text())
    tasks = []
    for product in products:
        relative = product.get('img', '').lstrip('/')
        asset = store / 'public' / relative if relative else None
        expected = product.get('imageSha256')
        matches = bool(asset and asset.is_file() and expected and
                       hashlib.sha256(asset.read_bytes()).hexdigest() == expected)
        if matches:
            action = 'reuse_approved'
        elif manifest.get('published') or product.get('status') == 'published':
            action = 'recover_published_asset'
        else:
            action = 'review_before_generation'
        tasks.append({'product': product['sharedProductId'], 'action': action})
    return {'batch': manifest.get('batch'), 'published': manifest.get('published', False),
            'generationAllowed': not manifest.get('published', False), 'tasks': tasks}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('batch', type=Path)
    parser.add_argument('--store', type=Path, required=True)
    args = parser.parse_args()
    print(json.dumps(check_batch(args.batch, args.store), ensure_ascii=False, indent=2))
