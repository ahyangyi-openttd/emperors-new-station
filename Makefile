.PHONY: rebuild all station clean_station clean doc.station cc.station

rebuild: clean all

all: station.grf

station: clean_station station.grf

clean_station:
	rm -f station.grf

clean:
	rm -f *.grf

doc.station:
	python3 -m station.ens doc
	cd docs; make html

station.grf:
	python3 -m station.ens gen

cc.station:
	opencc -i station/lang/chinese.lng -o station/lang/traditional_chinese.lng -c station/lang/opencc_config/s2t.json
	sed -i 's/##grflangid.*/##grflangid 0x0C/' station/lang/traditional_chinese.lng
