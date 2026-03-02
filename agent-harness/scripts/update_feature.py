#!/usr/bin/env python3
"""
Update feature pass/fail status in features.json
Supports Harness Engineering enhanced schema with completed_at timestamp
"""

import argparse
import json
import os
from datetime import datetime

def main():
    parser = argparse.ArgumentParser(description='Update feature status (Harness Engineering Edition)')
    parser.add_argument('--feature-index', type=int, required=True, help='Feature index (0-based)')
    parser.add_argument('--feature-id', type=str, help='Feature ID (alternative to index)')
    parser.add_argument('--passes', type=lambda x: x.lower() == 'true', required=True, help='True or False')
    parser.add_argument('--file', help='Features file path (default: .harness/features.json)')
    args = parser.parse_args()
    
    if args.file is None:
        default_harness_path = os.path.join('.harness', 'features.json')
        if os.path.exists(default_harness_path):
            args.file = default_harness_path
        elif os.path.exists('features.json'):
            args.file = 'features.json'
        else:
            args.file = default_harness_path

    if not os.path.exists(args.file):
        print(f"Error: Features file '{args.file}' does not exist")
        print("Please run setup_harness.py first to initialize the harness files.")
        return 1

    with open(args.file, 'r') as f:
        data = json.load(f)

    feature_index = args.feature_index
    
    if args.feature_id:
        for i, feature in enumerate(data['features']):
            if feature.get('id') == args.feature_id:
                feature_index = i
                break
        else:
            print(f"Error: Feature ID '{args.feature_id}' not found")
            return 1

    if feature_index >= len(data['features']):
        print(f"Error: Feature index {feature_index} out of range")
        return 1

    feature = data['features'][feature_index]
    old_status = feature['passes']
    feature['passes'] = args.passes
    
    if args.passes and not old_status:
        feature['completed_at'] = datetime.now().isoformat()
        print(f"Marked feature as passing at {feature['completed_at']}")
    elif not args.passes and 'completed_at' in feature:
        del feature['completed_at']

    with open(args.file, 'w') as f:
        json.dump(data, f, indent=2)

    feature_id = feature.get('id', f'index-{feature_index}')
    print(f"Updated feature {feature_id}: {old_status} -> {args.passes}")
    return 0

if __name__ == '__main__':
    exit(main())
