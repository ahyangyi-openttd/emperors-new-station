#!/usr/bin/env python
import grf
import argparse
from station.lib.docgen import gen_docs
from station.lib.parameters import parameter_list

import station.stations.railway_stations

metastations = [station.stations.railway_stations.the_stations]


def get_string_manager():
    s = grf.StringManager()
    s.import_lang_dir("station/lang", default_lang_file="english-uk.lng")
    return s


def gen(args):
    s = get_string_manager()
    g = grf.NewGRF(
        grfid=b"ENS_",
        name=s["STR_GRF_NAME"],
        description=s["STR_GRF_DESC"],
        version=0,
        min_compatible_version=0,
        id_map_file="station/id_map.json",
        sprite_cache_path="station/.cache",
        url="https://www.tt-forums.net/viewtopic.php?t=91092",
        strings=s,
        preferred_blitter=grf.NewGRF.BLITTER_BPP_32,
    )

    g.add(
        grf.ComputeParameters(
            target=0x40, operation=0x00, if_undefined=False, source1=0x11, source2=0xFE, value=b"\xff\xff\x00\x00"
        )
    )

    parameter_list.add(g, s)
    for metastation in metastations:
        if hasattr(metastation, "check_id_uniqueness"):
            metastation.check_id_uniqueness()
        g.add(metastation)

    g.write("ens.grf")


def docs(args):
    gen_docs(get_string_manager(), metastations)


def main():
    parser = argparse.ArgumentParser()

    subparsers = parser.add_subparsers(required=True)

    gen_parser = subparsers.add_parser("gen")
    gen_parser.set_defaults(func=gen)

    doc_parser = subparsers.add_parser("doc")
    doc_parser.set_defaults(func=docs)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
