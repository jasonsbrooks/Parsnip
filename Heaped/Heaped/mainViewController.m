//
//  mainViewController.m
//  Heaped
//
//  Created by Michael Zhao on 4/2/14.
//  Copyright (c) 2014 Michael Zhao. All rights reserved.
//

#import "mainViewController.h"
#import "HeapBeaconVC.h"
#import "ESTBeaconManager.h"
#import "ESTBeaconRegion.h"

@interface mainViewController () <ESTBeaconManagerDelegate>
@property ESTBeaconManager *beaconManager;
@property NSNumber *distance;
@end

@implementation mainViewController

- (id)initWithNibName:(NSString *)nibNameOrNil bundle:(NSBundle *)nibBundleOrNil
{
    self = [super initWithNibName:nibNameOrNil bundle:nibBundleOrNil];
    if (self) {
        // Custom initialization
    }
    return self;
}

- (void)viewDidLoad
{
    [super viewDidLoad];
	// Do any additional setup after loading the view.
    
    self.distance = [NSNumber numberWithInt:0];
    
    self.beaconManager = [[ESTBeaconManager alloc] init];
    self.beaconManager.delegate = self;
    self.beaconManager.avoidUnknownStateBeacons = YES;
    
    ESTBeaconRegion *region = [[ESTBeaconRegion alloc] init];
    
    [self.beaconManager startRangingBeaconsInRegion:region];
    
    [self setupView];
    
}

-(void)setupView
{
    /////////////////////////////////////////////////////////////
    // setup background image
    
    CGRect          screenRect          = [[UIScreen mainScreen] bounds];
    CGFloat         screenHeight        = screenRect.size.height;
    UIImageView*    backgroundImage;
    
    if (screenHeight > 480)
        backgroundImage = [[UIImageView alloc] initWithImage:[UIImage imageNamed:@"backgroundBig"]];
    else
        backgroundImage = [[UIImageView alloc] initWithImage:[UIImage imageNamed:@"backgroundSmall"]];
    
    [self.view addSubview:backgroundImage];

}

-(void)beaconManager:(ESTBeaconManager *)manager
     didRangeBeacons:(NSArray *)beacons
            inRegion:(ESTBeaconRegion *)region
{
    ESTBeacon* closestBeacon;
    
    if([beacons count] > 0)
    {
        // beacon array is sorted based on distance
        // closest beacon is the first one
        closestBeacon = [beacons objectAtIndex:0];
        
        // calculate and set new y position
        self.distance = closestBeacon.distance;
        
        NSLog([closestBeacon.distance stringValue]);
    }
}

- (void)didReceiveMemoryWarning
{
    [super didReceiveMemoryWarning];
    // Dispose of any resources that can be recreated.
}

- (IBAction)showDistance:(id)sender {
    self.distanceField.text = [self.distance stringValue];
}
@end
