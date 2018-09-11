#include <tiffio.h>

int main()
{
    TIFF *tif=TIFFOpen("../data/pop_clip.tif", "r");

	return 0;
}