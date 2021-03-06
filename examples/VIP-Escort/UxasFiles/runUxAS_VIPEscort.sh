SCRIPT_DIR="$( cd "$(dirname "$0")" ; pwd -P )"

cd $SCRIPT_DIR

RM_DATAWORK="rm -R ./datawork"
RM_LOG="rm -R ./log"

BIN="$UXAS_PATH/uxas"

mkdir -p RUNDIR_VIPEscort
cd RUNDIR_VIPEscort
$RM_DATAWORK
$RM_LOG
$BIN -cfgPath "$SCRIPT_DIR/cfg_VIPEscort.xml"
