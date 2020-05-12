import matplotlib.pyplot as plt
import geopandas as gpd

def scatterplot(df, figsize=(16,12), logx=False, logy=False):
    """Plot population vs amenities by category
    
    Args:
        df (DataFrame) : Amenities merged with population data
        figsize (tuple) : Figure size
        logx (bool) : Set x scale to log 
        logy (bool) : Set y scale to log
        
    Returns:
        None
    
    """
    nrows = 3
    ncols = 4
    fig, ax = plt.subplots(nrows=nrows, ncols=ncols, figsize=figsize, sharex=True)
    k = 0
    index = df.index.tolist()

    for i in range(nrows):
        for j in range(ncols):
            ax[i, j].scatter(df.loc["total_population"], df.iloc[k])
            ax[i, j].set_title(df.index[k])
            ax[i, j].set_xlabel('total_population')
            ax[i, j].set_title(f'{df.index[k].capitalize().replace("_", " ")}')
            ax[i, j].set_ylabel(f'Number of amenity in a borough')
            # ax[i, j].set_ylabel(f'Number of amenity in a borough (log)')
            ax[i, j].set_xlabel('Total population per borough')
            if logx:
                ax[i, j].set_xscale('log')
            if logy:
                ax[i, j].set_yscale('log')
            k += 1
            if k == 10:
                break

    fig.delaxes(ax[2, 2])
    fig.delaxes(ax[2, 3])
    fig.tight_layout()
    plt.show()
    
def choropleth(gdf, figsize=(20,20), cmap='viridis'):
    """Plot amenities types on map
    
    Args:
        gdf (GeoDataFrame) : Amenities data
        figsize (tuple) : Figure size
        cmap (str) : Color map
        
    Returns:
        None
    
    """
    nrows = 4
    ncols = 3
    fig, ax = plt.subplots(nrows=nrows, ncols=ncols, figsize=figsize, sharex=True)
    k = 0
    columns = gdf.columns[:-3]
    for i in range(nrows):
        for j in range(ncols):
            gdf.to_crs(epsg=3857).plot(column=columns[k], ax=ax[i, j], legend=True, scheme='fisher_jenks', cmap=cmap)
            ax[i, j].set_title(f'{columns[k].capitalize().replace("_", " ")}')
            ax[i, j].axis('off')
            k += 1
            if k == 10:
                break

    fig.delaxes(ax[3, 1])
    fig.delaxes(ax[3, 2])
    fig.tight_layout()